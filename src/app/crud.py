import logging
from typing import Any, List
from fastapi import HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import event
from sqlalchemy.orm import Session

from .meta_builder import set_metas

from .models.db_utils import validate_foreign_keys_before_insert
from .schemas.request_utils import FilterParams, RequestParams
from .models.db_models import Models

#  trace SQL requests - deactivate if not needed
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# attach event listeners to each Model for FK validation
for l_model in Models:
    for l_evt in ['before_insert','before_update']:
        event.listen(l_model, l_evt, validate_foreign_keys_before_insert)

def apply_filters(query: Query, model: Any, filters: List[FilterParams]) -> Query:
    """
    Apply FILTERS from params.filters.
    * key: str
    * value: Any
    * operator: str
    """
    for filter_param in filters:
        column = getattr(model, filter_param.key)
        if filter_param.operator == '==':
            if isinstance(filter_param.value, list):
                query = query.filter(column.in_(filter_param.value))
            else:
                query = query.filter(column == (filter_param.value))
        if filter_param.operator == '!=':
            if isinstance(filter_param.value, list):
                query = query.filter(~column.in_(filter_param.value))
            else:
                query = query.filter(column != (filter_param.value))
        if filter_param.operator == '>' and not isinstance(filter_param.value, list):
            query = query.filter(column > filter_param.value)
        if filter_param.operator == '>=' and not isinstance(filter_param.value, list):
            query = query.filter(column >= filter_param.value)
        if filter_param.operator == '<' and not isinstance(filter_param.value, list):
            query = query.filter(column < filter_param.value)
        if filter_param.operator == '<=' and not isinstance(filter_param.value, list):
            query = query.filter(column <= filter_param.value)
    return query


#  GET routes #

def get_all(db: Session, model: Any, params: RequestParams, bean: BaseModel):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    query = apply_filters(db.query(model), model, filters)
    query =  query.offset(skip + (limit * (page_nb - 1))).limit(limit).all()
    metas = set_metas(bean)
    return {"data": query, "metas": metas}

def get_one(id: int|str, db: Session, model: Any, params: RequestParams, bean: BaseModel):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    if filters != []:
        raise HTTPException(statusCode=405, detail={"msg": "No filter allowed for get_by_id Request"})
    # get columnObject to provide to filter()
    item_id = getattr(model, model.__tablename__ + '_id')
    query =  db.query(model).filter(item_id == id).first()
    if query is None:
        raise HTTPException(status_code=404, detail={"msg": "id not found", "key": model.__tablename__ + '_id', "value": id})
    metas = set_metas(bean)
    return {"data": query, "metas": metas}


# CREATE routes #

def create_one(db: Session, model: Any, bean: BaseModel):
    new_item = model(**bean.data.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


#  UPDATE routes #

def update_one(id: int|str, db: Session, model: Any, bean: BaseModel):
    # get columnObject to provide to filter()
    item_id = getattr(model, model.__tablename__ + '_id')
    #  retrieve existing item
    item = db.query(model).filter(item_id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail={"msg": "id not found", "key": model.__tablename__ + '_id', "value": id})
    #  update defined values
    for field, value in bean.data.model_dump().items():
        if value != None:
            setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item

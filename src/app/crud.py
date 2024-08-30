from typing import Any, List
from fastapi import HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import event
from sqlalchemy.orm import Session

from .models.db_utils import validate_foreign_keys_before_insert

from .schemas.request_utils import FilterParams, RequestParams
from .models.db_models import Booking, Comment, Guest, Invoice, Room

# attach event listeners to each Model for FK validation
event.listen(Booking, 'before_insert', validate_foreign_keys_before_insert)
event.listen(Comment, 'before_insert', validate_foreign_keys_before_insert)
event.listen(Guest, 'before_insert', validate_foreign_keys_before_insert)
event.listen(Invoice, 'before_insert', validate_foreign_keys_before_insert)
event.listen(Room, 'before_insert', validate_foreign_keys_before_insert)

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
            query = query.filter(column.like(filter_param.value))
        if filter_param.operator == '!=':
            query = query.filter(~column.like(filter_param.value))
        if filter_param.operator == '>':
            query = query.filter(column > filter_param.value)
        if filter_param.operator == '>=':
            query = query.filter(column >= filter_param.value)
        if filter_param.operator == '<':
            query = query.filter(column < filter_param.value)
        if filter_param.operator == '<=':
            query = query.filter(column <= filter_param.value)
    return query


#  GET routes #

def get_all(db: Session, model: Any, params: RequestParams):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    query = apply_filters(db.query(model), model, filters)
    query =  query.offset(skip + (limit * (page_nb - 1))).limit(limit).all()
    return query

def get_one(id: int|str, db: Session, model: Any, params: RequestParams):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    if filters != []:
        raise HTTPException(statusCode=405, detail={"msg": "No filter allowed for get_by_id Request"})
    # get columnObject to provide to filter()
    key_column = getattr(model, model.__tablename__ + '_id')
    query =  db.query(model).filter(key_column == id).first()
    if query is None:
        raise HTTPException(status_code=404, detail={"msg": "id not found", "key": model.__tablename__ + '_id', "value": id})
    return query


# CREATE routes #

def create_one(db: Session, model: Any, schema: BaseModel):
    new_object = model(**schema.model_dump())
    db.add(new_object)
    db.commit()
    db.refresh(new_object)
    return new_object
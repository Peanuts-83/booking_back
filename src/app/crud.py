from typing import List
from fastapi import HTTPException, Query
from pydantic import BaseModel
from pytest import param
from sqlalchemy.orm import Session

from .schemas.request_utils import FilterParams, RequestParams

def apply_filters(query: Query, model: BaseModel, filters: List[FilterParams]) -> Query:
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

def get_all(db: Session, model: BaseModel, params: RequestParams):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    query = apply_filters(db.query(model), model, filters)
    query =  query.offset(skip + (limit * (page_nb - 1))).limit(limit).all()
    return query

def get_one(id: int, db: Session, model: BaseModel, params: RequestParams):
    skip, limit, page_nb, filters = params.skip, params.limit, params.page_nb, params.filters
    if filters != []:
        raise HTTPException(statusCode=405, detail={"msg": "No filter allowed for get_by_id Request"})
    # get columnObject to provide to filter()
    key_column = getattr(model, model.__tablename__ + '_id')
    query =  db.query(model).filter(key_column == id).first()
    if query is None:
        raise HTTPException(status_code=404, detail={"msg": "id not found", "key": model.__tablename__ + '_id', "value": id})
    return query

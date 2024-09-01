
from typing import Any, List
from pydantic import BaseModel
from sqlalchemy import Boolean

class FilterParams(BaseModel):
    key: str
    value: Any
    operator: str

class RequestParams(BaseModel):
    skip: int = 0
    limit: int = 30
    page_nb: int = 1
    filters: list[FilterParams] = []

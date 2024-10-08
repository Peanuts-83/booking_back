
from email.mime import base
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.update import BookingUpdSchema

from ..schemas.create import BookingCreateSchema
from ..schemas.response import RespCreateSchema, RespGetAllSchema, RespGetOneSchema, RespUpdateSchema
from ..models.db_models import Booking

from .. import crud
from ..database import get_db
from ..schemas import schema
from ..schemas.request_utils import RequestParams


router = APIRouter()
model = Booking
baseBean = schema.BookingSchema

@router.post("/booking", response_model=RespGetAllSchema)
def get_all(params: RequestParams, db: Session = Depends(get_db)):
    """
    GET LIST

    Use params to filter data:
    * skip: int = 0
    * limit: int = 30
    * page_nb: int = 1
    * filters: list[FilterParams] = []
        * key: str
        * values: List[Any]
        * operator: str
    """
    result = crud.get_all(db, model, params, baseBean)
    return {"data": result['data'], "metas": result['metas'], "nb": len(result['data'])}

@router.post("/booking/get/{id}", response_model=RespGetOneSchema)
def get_one(id: str, params: RequestParams, db: Session = Depends(get_db)):
    """
    GET ONE BY ID
    """
    result = crud.get_one(id, db, model, params, baseBean)
    return {"data": result['data'], "metas": result['metas'], "nb": len([result['data']])}


@router.post("/booking/add", response_model=RespCreateSchema)
def create_one(bean: BookingCreateSchema, db: Session = Depends(get_db)):
    """
    CREATE new item > returns new item id
    """
    result = crud.create_one(db, model, bean)
    return {"id": getattr(result, 'id')}

@router.put("/booking/{id}", response_model=RespUpdateSchema)
def update_one(id: int, bean: BookingUpdSchema, db: Session = Depends(get_db)):
    """
    UPDATE item by id

    Bean.data contains only modified pairs [key: value]
    """
    result = crud.update_one(id, db, model, bean)
    return {"data": result, "nb": len([result])}
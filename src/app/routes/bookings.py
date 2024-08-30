
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.create import BookingCreateSchema
from ..schemas.response import RespCreateSchema, RespGetAllSchema, RespGetOneSchema
from ..models.db_models import Booking

from .. import crud
from ..database import get_db
from ..schemas import schema
from ..schemas.request_utils import RequestParams


router = APIRouter()
model = Booking

@router.post("/booking", response_model=RespGetAllSchema)
def get_all(params: RequestParams, db: Session = Depends
(get_db)):
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
    result = crud.get_all(db, model, params)
    return {"data": result, "nb": len(result)}

@router.post("/booking/get/{id}", response_model=RespGetOneSchema)
def get_one(id: int, params: RequestParams, db: Session = Depends(get_db)):
    """
    GET ONE by id
    """
    result = crud.get_one(id, db, model, params)
    return {"data": result, "nb": len([result])}


@router.post("/booking/add", response_model=RespCreateSchema)
def create_one(schema: BookingCreateSchema, db: Session = Depends(get_db)):
    """
    CREATE new item > returns new item id
    """
    result = crud.create_one(db, model, schema)
    return {"id": getattr(result, model.__tablename__ + '_id')}
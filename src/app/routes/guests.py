
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..schemas.update import GuestUpdSchema
from ..schemas.create import GuestCreateSchema
from ..schemas.response import RespCreateSchema, RespGetAllSchema, RespGetOneSchema, RespUpdateSchema
from ..models.db_models import Guest

from .. import crud
from ..database import get_db
from ..schemas import schema
from ..schemas.request_utils import RequestParams


router = APIRouter()
model = Guest

@router.post("/guest", response_model=RespGetAllSchema)
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

@router.post("/guest/get/{id}", response_model=RespGetOneSchema)
def get_one(id: str, params: RequestParams, db: Session = Depends(get_db)):
    """
    GET ONE BY ID
    """
    result = crud.get_one(id, db, model, params)
    return {"data": result, "nb": len([result])}


@router.post("/guest/add", response_model=RespCreateSchema)
def create_one(bean: GuestCreateSchema, db: Session = Depends(get_db)):
    """
    CREATE new item > returns new item id
    """
    result = crud.create_one(db, model, bean)
    return {"id": getattr(result, model.__tablename__ + '_id')}

@router.put("/guest/{id}", response_model=RespUpdateSchema)
def update_one(id: int, bean: GuestUpdSchema, db: Session = Depends(get_db)):
    """
    UPDATE item by id

    Bean.data contains only modified pairs [key: value]
    """
    result = crud.update_one(id, db, model, bean)
    return {"data": result, "nb": len([result])}

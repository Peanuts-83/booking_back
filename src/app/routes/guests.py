
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.db_models import Guest

from .. import crud
from ..database import get_db
from ..schemas import schemas
from ..schemas.request_utils import RequestParams


router = APIRouter()
model = Guest

@router.post("/guest", response_model=schemas.RespGetAllModel)
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

@router.post("/guest/{id}", response_model=schemas.RespGetOneModel)
def get_one(id: str, params: RequestParams, db: Session = Depends(get_db)):
    """
    GET ONE BY ID
    """
    result = crud.get_one(id, db, model, params)
    return {"data": result, "nb": len([result])}

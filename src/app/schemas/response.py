from typing import List
from pydantic import BaseModel

from ..meta_builder import Meta
from .schema import BookingSchema, CommentSchema, GuestSchema, InvoiceSchema, RoomSchema


class RespGetAllSchema(BaseModel):
    data: List[BookingSchema|CommentSchema|GuestSchema|InvoiceSchema|RoomSchema|None]
    metas: List[Meta]
    nb: int

class RespGetOneSchema(BaseModel):
    data: BookingSchema|CommentSchema|GuestSchema|InvoiceSchema|RoomSchema|None
    metas: List[Meta]
    nb: int

class RespCreateSchema(BaseModel):
    id: int|str

class RespUpdateSchema(BaseModel):
    data: BookingSchema|CommentSchema|GuestSchema|InvoiceSchema|RoomSchema|None
    nb: int
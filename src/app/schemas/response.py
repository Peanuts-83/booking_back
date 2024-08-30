from typing import List
from pydantic import BaseModel

from .schema import BookingSchema, CommentSchema, GuestSchema, InvoiceSchema, RoomSchema


class RespGetAllSchema(BaseModel):
    data: List[BookingSchema|CommentSchema|GuestSchema|InvoiceSchema|RoomSchema|None]
    nb: int

class RespGetOneSchema(BaseModel):
    data: BookingSchema|CommentSchema|GuestSchema|InvoiceSchema|RoomSchema|None
    nb: int

class RespCreateSchema(BaseModel):
    id: int|str
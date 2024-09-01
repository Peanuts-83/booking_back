
from datetime import date
from decimal import Decimal
from typing import Optional, Text
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


# TODO: remove payment_method (reserved to invoice table!)
class BookingCreate(BaseModel):
    guest_id: Optional[str] = Field(max_length=40, min_length=36)
    check_in_date: Optional[date] = Field()
    check_out_date: Optional[date] = Field()
    num_guests: Optional[int] = Field(ge=0)
    is_checked_in: Optional[bool] = Field()
    room_id: Optional[int] = Field(ge=1, le=55)
    invoice_id: Optional[int] = Field()

    @validator('check_out_date')
    def check_date_validity(cls, v, values):
        if v < values['check_in_date']:
            raise HTTPException(status_code=409, detail={"msg": "check_out_date before check_in_date", "key": 'check_out_date', "value": v})
        return v
class BookingCreateSchema(BaseModel):
    data: BookingCreate



class CommentCreate(BaseModel):
    guest_id: Optional[str] = Field()
    comment_date: Optional[date] = Field()
    comment_rating: Optional[int] = Field(ge=1, le=5)
    comment_text: Optional[Text] = Field(max_length=500)
    room_id: Optional[int] = Field(ge=1, le=55)
class CommentCreateSchema(BaseModel):
    data: CommentCreate



class GuestCreate(BaseModel):
    first_name: Optional[str] = Field()
    last_name: Optional[str] = Field()
    age: Optional[int] = Field(ge=1, le=130)
    country: Optional[str] = Field()
    phone_number: Optional[str] = Field()
    email: Optional[str] = Field(pattern="^\w+@\w+\.[a-z]{2,}$")
    gold_card_member: Optional[bool] = Field(default=False)
class GuestCreateSchema(BaseModel):
    data: GuestCreate



class InvoiceCreate(BaseModel):
    invoice_date: Optional[date] = Field()
    guest_id: Optional[str] = Field()
    total_amount: Optional[Decimal] = Field()
    payment_method: Optional[str] = Field(pattern="^(PayPal|Bank Tranfer|Cash|Credit Card)$")
    due_date: Optional[date] = Field()
    item_description: Optional[str] = Field(max_length=200)
    quantity: Optional[int] = Field()
    room_id: Optional[int] = Field(ge=1, le=55)
class InvoiceCreateSchema(BaseModel):
    data: InvoiceCreate



class RoomCreate(BaseModel):
    room_type: Optional[str] = Field(pattern="^(single|double|suite)$")
    price_per_night: Optional[Decimal] = Field()
    availability: Optional[bool] = Field(default=True)
class RoomCreateSchema(BaseModel):
    data: RoomCreate
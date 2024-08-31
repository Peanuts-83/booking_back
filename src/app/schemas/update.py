from datetime import date
from decimal import Decimal
from typing import Optional, Text
from fastapi import HTTPException
from pydantic import BaseModel, Field, ValidationError, constr, validator


class BookingUpdate(BaseModel):
    ref_guest_id: Optional[str] = Field(default=None, max_length=40, min_length=36)
    check_in_date: Optional[date] = Field(default=None)
    check_out_date: Optional[date] = Field(default=None)
    num_guests: Optional[int] = Field(default=None, ge=0)
    is_checked_in: Optional[bool] = Field(default=None)
    ref_room_id: Optional[int] = Field(default=None, ge=1, le=55)
    ref_invoice_id: Optional[int] = Field(default=None)

    @validator('check_out_date')
    def check_date_validity(cls, v, values):
        if v < values['check_in_date']:
            raise HTTPException(status_code=409, detail={"msg": "check_out_date before check_in_date", "key": 'check_out_date', "value": v})
        return v

class BookingUpdSchema(BaseModel):
    data: BookingUpdate




class CommentUpdate(BaseModel):
    ref_guest_id: Optional[str] = Field(default=None)
    comment_date: Optional[date] = Field(default=None)
    comment_rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment_text: Optional[Text] = Field(default=None, max_length=500)
    ref_room_id: Optional[int] = Field(default=None, ge=1, le=55)
class CommentUpdSchema(BaseModel):
    data: CommentUpdate



class GuestUpdate(BaseModel):
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None, ge=1, le=130)
    country: Optional[str] = Field(default=None)
    phone_number: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None, pattern="^\w+@\w+\.[a-z]{2,}$")
    gold_card_member: Optional[bool] = Field(default=None)
class GuestUpdSchema(BaseModel):
    data: GuestUpdate



class InvoiceUpdate(BaseModel):
    invoice_date: Optional[date] = Field(default=None)
    ref_guest_id: Optional[str] = Field(default=None)
    total_amount: Optional[Decimal] = Field(default=None)
    payment_method: Optional[str] = Field(default=None, pattern="^(PayPal|Bank Tranfer|Cash|Credit Card)$")
    due_date: Optional[date] = Field(default=None)
    item_description: Optional[str] = Field(default=None, max_length=200)
    quantity: Optional[int] = Field(default=None)
    ref_room_id: Optional[int] = Field(default=None, ge=1, le=55)
class InvoiceUpdSchema(BaseModel):
    data: InvoiceUpdate



class RoomUpdate(BaseModel):
    room_type: Optional[str] = Field(default=None, pattern="^(single|double|suite)$")
    price_per_night: Optional[Decimal] = Field(default=None)
    availability: Optional[bool] = Field(default=None)
class RoomUpdSchema(BaseModel):
    data: RoomUpdate
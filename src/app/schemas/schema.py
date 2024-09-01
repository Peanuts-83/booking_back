from datetime import date
from decimal import Decimal
from typing import Optional, Text
from pydantic import BaseModel

class BookingSchema(BaseModel):
    id: int
    guest_id: Optional[str]
    check_in_date: date
    check_out_date: date
    num_guests: int
    is_checked_in: bool
    room_id: Optional[int]
    invoice_id: Optional[int]

class CommentSchema(BaseModel):
    id: int
    guest_id: Optional[str]
    comment_date: date
    comment_rating: int
    comment_text: Text
    room_id: Optional[int]

class GuestSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    age: int
    country: str
    phone_number: str
    email: str
    gold_card_member: bool

class InvoiceSchema(BaseModel):
    id: int
    invoice_date: date
    guest_id: Optional[str]
    total_amount: Decimal
    payment_method: str
    due_date: date
    item_description: str
    quantity: int
    room_id: Optional[int]

class RoomSchema(BaseModel):
    id: int
    room_type: str
    price_per_night: Decimal
    availability: bool

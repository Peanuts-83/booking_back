from datetime import date
from decimal import Decimal
from typing import Optional, Text
from pydantic import BaseModel

class BookingSchema(BaseModel):
    booking_id: int
    ref_guest_id: Optional[str]
    check_in_date: date
    check_out_date: date
    num_guests: int
    is_checked_in: bool
    ref_room_id: Optional[int]
    ref_invoice_id: Optional[int]

class CommentSchema(BaseModel):
    comment_id: int
    ref_guest_id: Optional[str]
    comment_date: date
    comment_rating: int
    comment_text: Text
    ref_room_id: Optional[int]

class GuestSchema(BaseModel):
    guest_id: str
    first_name: str
    last_name: str
    age: int
    country: str
    phone_number: str
    email: str
    gold_card_member: bool

class InvoiceSchema(BaseModel):
    invoice_id: int
    invoice_date: date
    ref_guest_id: Optional[str]
    total_amount: Decimal
    payment_method: str
    due_date: date
    item_description: str
    quantity: int
    ref_room_id: Optional[int]

class RoomSchema(BaseModel):
    room_id: int
    room_type: str
    price_per_night: Decimal
    availability: bool

from datetime import date
from decimal import Decimal
from typing import Optional, Text
from pydantic import BaseModel

class BookingSchema(BaseModel):
    booking_id: int
    ref_guest_id: Optional[str]
    check_in_date: Optional[date]
    check_out_date: Optional[date]
    num_guests: Optional[int]
    is_checked_in: Optional[bool]
    ref_room_id: Optional[int]
    ref_invoice_id: Optional[int]

class CommentSchema(BaseModel):
    comment_id: int
    ref_guest_id: Optional[str]
    comment_date: Optional[date]
    comment_rating: Optional[int]
    comment_text: Optional[Text]
    ref_room_id: Optional[int]

class GuestSchema(BaseModel):
    guest_id: str
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    country: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    gold_card_member: Optional[bool]

class InvoiceSchema(BaseModel):
    invoice_id: int
    invoice_date: Optional[date]
    ref_guest_id: Optional[str]
    total_amount: Optional[Decimal]
    payment_method: Optional[str]
    due_date: Optional[date]
    item_description: Optional[str]
    quantity: Optional[int]
    ref_room_id: Optional[int]

class RoomSchema(BaseModel):
    room_id: int
    room_type: Optional[str]
    price_per_night: Optional[Decimal]
    availability: Optional[bool]

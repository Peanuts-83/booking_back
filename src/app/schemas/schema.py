from datetime import date
from decimal import Decimal
from typing import Text
from pydantic import BaseModel

class BookingSchema(BaseModel):
    booking_id: int
    ref_guest_id: str
    check_in_date: date | None
    check_out_date: date | None
    num_guests: int | None
    payment_method: str | None
    is_checked_in: bool | None
    ref_room_id: int
    ref_invoice_id: int | None

class CommentSchema(BaseModel):
    comment_id: int
    ref_guest_id: str
    comment_date: date
    comment_rating: int
    comment_text: Text
    room_number: int

class GuestSchema(BaseModel):
    guest_id: str
    first_name: str
    last_name: str
    age: int
    country: str
    phone_number: str|None
    email: str|None
    gold_card_member: bool

class InvoiceSchema(BaseModel):
    invoice_id: int
    invoice_date: date
    ref_guest_id: str
    total_amount: Decimal
    payment_method: str
    due_date: date
    item_description: str
    quantity: int
    ref_room_id: int

class RoomSchema(BaseModel):
    room_id: int
    room_type: str
    price_per_night: Decimal
    availability: bool

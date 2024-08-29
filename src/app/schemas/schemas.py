from datetime import date
from decimal import Decimal
from pydantic import BaseModel

class BookingModel(BaseModel):
    booking_id: int
    ref_guest_id: str
    check_in_date: date | None
    check_out_date: date | None
    num_guests: int | None
    payment_method: str | None
    is_checked_in: bool | None
    ref_room_id: int
    ref_invoice_id: int | None

class CommentModel(BaseModel):
    comment_id: int
    ref_guest_id: str
    comment_date: date
    comment_rating: int
    room_number: int

class GuestModel(BaseModel):
    guest_id: str
    first_name: str
    last_name: str
    age: int
    country: str
    phone_number: str
    email: str
    gold_card_member: bool

class InvoiceModel(BaseModel):
    invoice_id: int
    invoice_date: date
    ref_guest_id: str
    total_amount: Decimal
    payment_method: str
    due_date: date
    item_description: str
    quantity: int
    ref_room_id: int

class RoomModel(BaseModel):
    room_id: int
    room_type: str
    price_per_night: Decimal
    availability: bool

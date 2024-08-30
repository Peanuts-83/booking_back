
from datetime import date
from pydantic import BaseModel


class BookingCreateSchema(BaseModel):
    ref_guest_id: str
    check_in_date: date | None
    check_out_date: date | None
    num_guests: int | None
    payment_method: str | None
    is_checked_in: bool | None
    ref_room_id: int
    ref_invoice_id: int | None

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class BookingUpdate(BaseModel):
    ref_guest_id: Optional[str] = Field(default=None)
    check_in_date: Optional[date] = Field(default=None)
    check_out_date: Optional[date] = Field(default=None)
    num_guests: Optional[int] = Field(default=None)
    payment_method: Optional[str] = Field(default=None)
    is_checked_in: Optional[bool] = Field(default=None)
    ref_room_id: Optional[int] = Field(default=None)
    ref_invoice_id: Optional[int] = Field(default=None)

class BookingUpdSchema(BaseModel):
    data: BookingUpdate


try:
    BookingUpdSchema(data={"ref_guest_id":None})
except ValidationError as e:
    print(e.errors())
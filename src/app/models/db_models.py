from sqlalchemy import DECIMAL, Boolean, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.orm import relationship

from ..database import Base


class Booking(Base):
    __tablename__ = 'booking'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    ref_guest_id = Column(String(40), ForeignKey('guest.guest_id'), nullable=True)
    check_in_date = Column(Date, nullable=True)
    check_out_date = Column(Date, nullable=True)
    num_guests = Column(Integer, nullable=True)
    payment_method = Column(String(11), nullable=True)
    is_checked_in = Column(Boolean, nullable=True)
    ref_room_id = Column(Integer, ForeignKey('room.room_id'), nullable=True)
    ref_invoice_id = Column(Integer, ForeignKey('invoice.invoice_id'), nullable=True)

    # Relationships (optional, but useful for ORM)
    guest = relationship("Guest", back_populates="booking")
    room = relationship("Room", back_populates="booking")
    invoice = relationship("Invoice", back_populates="booking")


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    ref_guest_id = Column(String(40), ForeignKey('guest.guest_id'), nullable=True)
    comment_date = Column(Date, nullable=False)
    comment_rating = Column(Integer, nullable=False)
    comment_text = Column(Text, nullable=True)
    room_number = Column(Integer, nullable=False)

    guest = relationship("Guest", back_populates="comment")


class Guest(Base):
    __tablename__ = 'guest'
    guest_id = Column(String(40), primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    country = Column(String(50), nullable=True)
    phone_number = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    gold_card_member = Column(Boolean, nullable=True)

    booking = relationship('Booking', back_populates='guest')
    invoice = relationship('Invoice', back_populates='guest')
    comment = relationship('Comment', back_populates='guest')


class Invoice(Base):
    __tablename__ = 'invoice'
    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(Date, nullable=True)
    ref_guest_id = Column(String(40), ForeignKey('guest.guest_id'), nullable=True)
    total_amount = Column(DECIMAL(15,2), nullable=True)
    payment_method = Column(String(13), nullable=True)
    due_date = Column(Date, nullable=True)
    item_description = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=True)
    ref_room_id=  Column(Integer, ForeignKey('room.room_id'), nullable=True)

    guest = relationship("Guest", back_populates="invoice")
    room = relationship("Room", back_populates="invoice")
    booking = relationship('Booking', back_populates='invoice')



class Room(Base):
    __tablename__ = 'room'
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    room_type = Column(String(6), nullable=True)
    price_per_night = Column(DECIMAL(15,2), nullable=True)
    availability = Column(Boolean, nullable=True)

    booking = relationship('Booking', back_populates='room')
    invoice = relationship('Invoice', back_populates='room')

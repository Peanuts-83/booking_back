from uuid import uuid4
from sqlalchemy import DECIMAL, Boolean, Column, Integer, String, Date, ForeignKey, Text, func
from sqlalchemy.orm import relationship

from ..database import Base


class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(String(40), ForeignKey(column='guest.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)
    check_in_date = Column(Date, nullable=True)
    check_out_date = Column(Date, nullable=True)
    num_guests = Column(Integer, nullable=True)
    is_checked_in = Column(Boolean, nullable=True)
    room_id = Column(Integer, ForeignKey(column='room.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)
    invoice_id = Column(Integer, ForeignKey(column='invoice.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)

    # Relationships (optional, but useful for ORM)
    # guest = relationship("Guest", back_populates="booking")
    # room = relationship("Room", back_populates="booking")
    # invoice = relationship("Invoice", back_populates="booking")


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    guest_id = Column(String(40), ForeignKey(column='guest.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)
    comment_date = Column(Date, nullable=False)
    comment_rating = Column(Integer, nullable=False)
    comment_text = Column(Text, nullable=True)
    room_id = Column(Integer, ForeignKey(column='room.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)

    # guest = relationship("Guest", back_populates="comment")


class Guest(Base):
    __tablename__ = 'guest'
    id = Column(String(40), primary_key=True, default=lambda: str(uuid4()))
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    country = Column(String(50), nullable=True)
    phone_number = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    gold_card_member = Column(Boolean, nullable=True)

    # booking = relationship('Booking', back_populates='guest')
    # invoice = relationship('Invoice', back_populates='guest_id')
    # comment = relationship('Comment', back_populates='guest_id')


class Invoice(Base):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(Date, nullable=True)
    guest_id = Column(String(40), ForeignKey(column='guest.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)
    total_amount = Column(DECIMAL(15,2), nullable=True)
    payment_method = Column(String(13), nullable=True)
    due_date = Column(Date, nullable=True)
    item_description = Column(Text, nullable=True)
    quantity = Column(Integer, nullable=True)
    room_id=  Column(Integer, ForeignKey(column='room.id', onupdate='CASCADE', ondelete='NULL'), nullable=True)

    # guest = relationship("Guest", back_populates="invoice")
    # room = relationship("Room", back_populates="invoice")



class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_type = Column(String(6), nullable=True)
    price_per_night = Column(DECIMAL(15,2), nullable=True)
    availability = Column(Boolean, nullable=True)

    # booking = relationship('Booking', back_populates='room')
    # invoice = relationship('Invoice', back_populates='room')


Models = [Booking, Comment, Guest, Invoice, Room]

from typing import Optional
import datetime

from sqlalchemy import Boolean, Column, Date, Double, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, Table, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = 'address'
    __table_args__ = (
        PrimaryKeyConstraint('address_id', name='address_pkey'),
    )

    address_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street_address: Mapped[Optional[str]] = mapped_column(Text)
    address_line2: Mapped[Optional[str]] = mapped_column(Text)
    city: Mapped[Optional[str]] = mapped_column(Text)
    state_province: Mapped[Optional[str]] = mapped_column(Text)
    postal_code: Mapped[Optional[str]] = mapped_column(Text)
    country: Mapped[Optional[str]] = mapped_column(Text)

    venue: Mapped[Optional['Venue']] = relationship('Venue', uselist=False, back_populates='address')


class AppUser(Base):
    __tablename__ = 'app_user'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='app_user_pkey'),
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)
    phone_number: Mapped[Optional[str]] = mapped_column(Text)
    email: Mapped[Optional[str]] = mapped_column(Text)
    is_admin: Mapped[Optional[bool]] = mapped_column(Boolean)
    venue_owner: Mapped[Optional[bool]] = mapped_column(Boolean)

    venue: Mapped[list['Venue']] = relationship('Venue', back_populates='owner')


class EventOrganizer(AppUser):
    __tablename__ = 'event_organizer'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['app_user.user_id'], name='event_organizer_user_id_fkey'),
        PrimaryKeyConstraint('user_id', name='event_organizer_pkey')
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    speciality: Mapped[Optional[str]] = mapped_column(Text)

    event_info: Mapped[list['EventInfo']] = relationship('EventInfo', back_populates='event_organizer')


class Performer(AppUser):
    __tablename__ = 'performer'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['app_user.user_id'], name='performer_user_id_fkey'),
        PrimaryKeyConstraint('user_id', name='performer_pkey')
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    band_name: Mapped[Optional[str]] = mapped_column(Text)
    type: Mapped[Optional[str]] = mapped_column(Text, comment='artist, comedian etc.')
    crewsize: Mapped[Optional[int]] = mapped_column(Integer)

    event: Mapped[list['EventInfo']] = relationship('EventInfo', secondary='event_performers', back_populates='performer')


class Venue(Base):
    __tablename__ = 'venue'
    __table_args__ = (
        ForeignKeyConstraint(['address_id'], ['address.address_id'], name='venue_address_id_fkey'),
        ForeignKeyConstraint(['owner_id'], ['app_user.user_id'], name='venue_owner_id_fkey'),
        PrimaryKeyConstraint('venue_id', name='venue_pkey'),
        UniqueConstraint('address_id', name='venue_address_id_key')
    )

    venue_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(Text)
    capacity: Mapped[Optional[int]] = mapped_column(Integer)
    owner_id: Mapped[Optional[int]] = mapped_column(Integer)

    address: Mapped[Optional['Address']] = relationship('Address', back_populates='venue')
    owner: Mapped[Optional['AppUser']] = relationship('AppUser', back_populates='venue')
    dates_unavailable: Mapped[list['DatesUnavailable']] = relationship('DatesUnavailable', back_populates='venue')
    event_info: Mapped[list['EventInfo']] = relationship('EventInfo', back_populates='venue')


class DatesUnavailable(Base):
    __tablename__ = 'dates_unavailable'
    __table_args__ = (
        ForeignKeyConstraint(['venue_id'], ['venue.venue_id'], name='dates_unavailable_venue_id_fkey'),
        PrimaryKeyConstraint('availability_id', name='dates_unavailable_pkey')
    )

    availability_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    venue_id: Mapped[Optional[int]] = mapped_column(Integer)
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    venue: Mapped[Optional['Venue']] = relationship('Venue', back_populates='dates_unavailable')


class EventInfo(Base):
    __tablename__ = 'event_info'
    __table_args__ = (
        ForeignKeyConstraint(['organizer'], ['event_organizer.user_id'], name='event_info_organizer_fkey'),
        ForeignKeyConstraint(['venue_id'], ['venue.venue_id'], name='event_info_venue_id_fkey'),
        PrimaryKeyConstraint('event_id', name='event_info_pkey')
    )

    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    venue_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)
    organizer: Mapped[Optional[int]] = mapped_column(Integer)

    event_organizer: Mapped[Optional['EventOrganizer']] = relationship('EventOrganizer', back_populates='event_info')
    venue: Mapped[Optional['Venue']] = relationship('Venue', back_populates='event_info')
    performer: Mapped[list['Performer']] = relationship('Performer', secondary='event_performers', back_populates='event')
    event_datetime: Mapped[list['EventDatetime']] = relationship('EventDatetime', back_populates='event')
    ticket: Mapped[list['Ticket']] = relationship('Ticket', back_populates='event')


class EventDatetime(Base):
    __tablename__ = 'event_datetime'
    __table_args__ = (
        ForeignKeyConstraint(['event_id'], ['event_info.event_id'], name='event_datetime_event_info_id_fkey'),
        PrimaryKeyConstraint('dt_id', name='event_datetime_pkey')
    )

    dt_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[Optional[int]] = mapped_column(Integer)
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    start_time: Mapped[Optional[str]] = mapped_column(Text)
    end_time: Mapped[Optional[str]] = mapped_column(Text)

    event: Mapped[Optional['EventInfo']] = relationship('EventInfo', back_populates='event_datetime')


t_event_performers = Table(
    'event_performers', Base.metadata,
    Column('performer_id', Integer, primary_key=True),
    Column('event_id', Integer, primary_key=True),
    ForeignKeyConstraint(['event_id'], ['event_info.event_id'], name='event_performers_event_id_fkey'),
    ForeignKeyConstraint(['performer_id'], ['performer.user_id'], name='event_performers_performer_id_fkey'),
    PrimaryKeyConstraint('performer_id', 'event_id', name='event_performers_pkey')
)


class Ticket(Base):
    __tablename__ = 'ticket'
    __table_args__ = (
        ForeignKeyConstraint(['event_id'], ['event_info.event_id'], name='ticket_event_id_fkey'),
        PrimaryKeyConstraint('event_id', 'ticket_id', name='ticket_pkey')
    )

    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticket_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[Optional[float]] = mapped_column(Double(53))
    ticket_sold: Mapped[Optional[bool]] = mapped_column(Boolean)

    event: Mapped['EventInfo'] = relationship('EventInfo', back_populates='ticket')

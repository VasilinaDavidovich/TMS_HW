from __future__ import annotations
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey, select
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(30))
    points: Mapped[int] = mapped_column(Integer, default=0)

    @staticmethod
    def is_exist(session: Session, username: str) -> bool:
        stmt = select(User).where(User.username == username)
        result = session.scalars(stmt).first()
        return result is not None

    def orders(self, session: Session) -> list['Order']:
        stmt = select(Order).where(Order.user_id == self.id)
        return list(session.scalars(stmt).all())

class Ticket(Base):
    __tablename__ = 'tickets'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, default=True)
    user: Mapped[int] = mapped_column(ForeignKey("users.id"))

    @staticmethod
    def valid_ticket(session: Session, ticket_uuid: str) -> bool:
        return session.query(
            session.query(Ticket)
            .filter(Ticket.uuid == ticket_uuid)
            .filter(Ticket.available == True)
            .exists()
        ).scalar()

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    cost: Mapped[int] = mapped_column(Integer(), nullable=False)
    count: Mapped[int] = mapped_column(Integer(), nullable=False)

class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    count: Mapped[int] = mapped_column(Integer(), nullable=False)
    order_datetime: Mapped[datetime] = mapped_column(DateTime())




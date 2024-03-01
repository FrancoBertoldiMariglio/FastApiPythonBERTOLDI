from enum import Enum as PyEnum

from sqlalchemy import Column, Float, DateTime, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class DeliveryMethod(PyEnum):
    DRIVE_THRU = 1
    ON_HAND = 2
    HOME_DELIVERY = 3


class Status(PyEnum):
    PENDING = 1
    IN_PROGRESS = 2
    DELIVERED = 3
    CANCELED = 4


class OrderModel(BaseModel):
    __tablename__ = "orders"

    date = Column(DateTime)
    total = Column(Float)
    delivery_method = Column(Enum(DeliveryMethod))
    status = Column(Enum(Status))
    client_id = Column(Integer, ForeignKey('clients.id_key'))
    bill_id = Column(Integer, ForeignKey('bills.id_key'))

    order_details = relationship("OrderDetailModel", back_populates="order", cascade="all, delete-orphan",
                                 lazy="joined")
    client = relationship("ClientModel", back_populates="orders", lazy="joined")
    bill = relationship("BillModel", back_populates="order", lazy="joined")

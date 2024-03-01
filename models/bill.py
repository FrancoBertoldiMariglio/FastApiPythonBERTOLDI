from enum import Enum as PyEnum

from sqlalchemy import Column, String, Float, Date, Enum
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class PaymentType(PyEnum):
    CASH = "cash"
    CARD = "card"


class BillModel(BaseModel):
    __tablename__ = "bills"

    bill_number = Column(String, index=True)
    discount = Column(Float)
    date = Column(Date)
    total = Column(Float)
    payment_type = Column(Enum(PaymentType))
    order = relationship('OrderModel', back_populates='bill', uselist=False, lazy="joined")

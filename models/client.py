from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ClientModel(BaseModel):
    __tablename__ = "clients"

    name = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String)
    telephone = Column(String)

    addresses = relationship("AddressModel", back_populates="client", cascade="all, delete-orphan", lazy="joined")
    orders = relationship("OrderModel", back_populates="client", cascade="all, delete-orphan", lazy="joined")

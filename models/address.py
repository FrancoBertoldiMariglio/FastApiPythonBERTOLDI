"""
Module for the AddressModel class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class AddressModel(BaseModel):
    """
    AddressModel class with attributes and relationships.
    """
    __tablename__ = 'addresses'

    street = Column(String, index=True)
    number = Column(String)
    city = Column(String)
    client_id = Column(Integer, ForeignKey('clients.id_key'))
    client = relationship('ClientModel', back_populates='addresses', lazy='joined')

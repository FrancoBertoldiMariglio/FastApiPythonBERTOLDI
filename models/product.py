"""
SqlAlchemy model for products.

This module defines the ProductModel class which represents a product in the database.
"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class ProductModel(BaseModel):
    """
    Class representing a product in the database.

    This class represents a product. It inherits from BaseModel and adds additional fields
    specific to products: name, price, and category_id. It also defines relationships with
    CategoryModel, ReviewModel, and OrderDetailModel.
    """

    __tablename__ = 'products'

    name = Column(String, index=True)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id_key'))

    category = relationship(
        'CategoryModel',
        back_populates='products',
        lazy='joined',
    )
    reviews = relationship(
        'ReviewModel',
        back_populates='product',
        cascade='all, delete-orphan',
        lazy='joined',
    )
    order_details = relationship(
        'OrderDetailModel',
        back_populates='product',
        cascade='all, delete-orphan',
        lazy='joined',
    )

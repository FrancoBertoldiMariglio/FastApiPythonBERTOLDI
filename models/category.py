from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    name = Column(String, unique=True, index=True)
    products = relationship('ProductModel', back_populates='category', lazy="joined")

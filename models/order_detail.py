from sqlalchemy import Column, Float, INT, ForeignKey, Integer
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class OrderDetailModel(BaseModel):
    __tablename__ = "order_details"

    quantity = Column(INT)
    price = Column(Float)
    order_id = Column(INT, ForeignKey("orders.id_key"))
    product_id = Column(Integer, ForeignKey("products.id_key"))

    order = relationship("OrderModel", back_populates="order_details", lazy="joined")
    product = relationship("ProductModel", back_populates="order_details", lazy="joined")

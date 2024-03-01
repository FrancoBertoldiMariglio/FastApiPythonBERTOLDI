from typing import Optional, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.order_schema import OrderSchema
    from schemas.product_schema import ProductSchema


class OrderDetailSchema(BaseSchema):
    quantity: Optional[int] = None
    price: Optional[float] = None

    order_id: Optional[int] = None
    product_id: Optional[int] = None

    order: Optional['OrderSchema'] = None
    product: Optional['ProductSchema'] = None

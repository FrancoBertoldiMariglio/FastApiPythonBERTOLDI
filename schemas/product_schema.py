from typing import Optional, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.category_schema import CategorySchema
    from schemas.order_detail_schema import OrderDetailSchema
    from schemas.review_schema import ReviewSchema


class ProductSchema(BaseSchema):
    name: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

    category_id: Optional[int] = None

    category: Optional['CategorySchema'] = None
    reviews: Optional['ReviewSchema'] = None
    order_details: Optional['OrderDetailSchema'] = None

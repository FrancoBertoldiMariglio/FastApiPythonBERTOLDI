from typing import Optional, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.product_schema import ProductSchema


class ReviewSchema(BaseSchema):
    raiting: Optional[float] = None
    comment: Optional[str] = None
    product_id: Optional[int] = None
    product: Optional['ProductSchema'] = None

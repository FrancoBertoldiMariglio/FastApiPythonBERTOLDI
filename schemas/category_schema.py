# CategorySchema
from typing import Optional, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.product_schema import ProductSchema


class CategorySchema(BaseSchema):
    name: Optional[str] = None
    product: Optional['ProductSchema'] = None

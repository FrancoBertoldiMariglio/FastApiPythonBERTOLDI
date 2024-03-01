from typing import Optional, List, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.address_schema import AddressSchema
    from schemas.order_schema import OrderSchema


class ClientSchema(BaseSchema):
    name: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    telephone: Optional[str] = None
    addresses: Optional[List['AddressSchema']] = []
    orders: Optional[List['OrderSchema']] = []

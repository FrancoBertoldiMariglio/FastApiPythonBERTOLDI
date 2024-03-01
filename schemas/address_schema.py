from typing import Optional

from schemas.base_schema import BaseSchema


class AddressSchema(BaseSchema):
    street: Optional[str] = None
    number: Optional[str] = None
    city: Optional[str] = None
    client_id: int

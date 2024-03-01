from typing import Dict, Type

from schemas.base_schema import BaseSchema


class NestedSchema(BaseSchema):
    schemas: Dict[str, BaseSchema]

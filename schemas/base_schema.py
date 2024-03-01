from typing import Optional

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

    id_key: Optional[int] = None

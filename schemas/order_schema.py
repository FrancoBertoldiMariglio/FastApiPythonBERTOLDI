from datetime import datetime
from enum import Enum
from typing import Optional

from schemas.base_schema import BaseSchema


class DeliveryMethod(Enum):
    DRIVE_THRU = 1
    ON_HAND = 2
    HOME_DELIVERY = 3


class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    DELIVERED = 3
    CANCELED = 4


class OrderSchema(BaseSchema):
    date: Optional[datetime] = None
    total: Optional[float] = None
    delivery_method: DeliveryMethod
    status: Status
    client_id: int
    bill_id: int

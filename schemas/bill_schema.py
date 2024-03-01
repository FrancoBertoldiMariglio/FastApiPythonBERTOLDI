from enum import Enum
from typing import Optional, TYPE_CHECKING

from schemas.base_schema import BaseSchema

if TYPE_CHECKING:
    from schemas.order_schema import OrderSchema


class PaymentType(Enum):
    CASH = "cash"
    CARD = "card"


class BillSchema(BaseSchema):
    bill_number: Optional[str] = None
    discount: Optional[float] = None
    date: Optional[str] = None
    total: Optional[float] = None
    payment_type: Optional[PaymentType] = None
    order: Optional['OrderSchema'] = None

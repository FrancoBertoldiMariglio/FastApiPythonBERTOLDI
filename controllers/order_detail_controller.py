from controllers.base_controller_impl import BaseControllerImpl
from schemas.order_detail_schema import OrderDetailSchema
from services.order_detail_service import OrderDetailService


class OrderDetailController(BaseControllerImpl):
    def __init__(self):
        super().__init__(OrderDetailSchema, OrderDetailService())

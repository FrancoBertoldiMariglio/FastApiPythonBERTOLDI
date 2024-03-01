from controllers.base_controller_impl import BaseControllerImpl
from schemas.order_schema import OrderSchema
from services.order_service import OrderService


class OrderController(BaseControllerImpl):
    def __init__(self):
        super().__init__(OrderSchema, OrderService())

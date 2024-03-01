from models.order import OrderModel
from repositories.order_repository import OrderRepository
from schemas.order_schema import OrderSchema
from services.base_service_impl import BaseServiceImpl


class OrderService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=OrderRepository(), model=OrderModel, schema=OrderSchema)

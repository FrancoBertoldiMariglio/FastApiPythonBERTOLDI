from models.order import OrderModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import OrderSchema


class OrderRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(OrderModel, OrderSchema)

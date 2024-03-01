from models.order_detail import OrderDetailModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import OrderDetailSchema


class OrderDetailRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(OrderDetailModel, OrderDetailSchema)

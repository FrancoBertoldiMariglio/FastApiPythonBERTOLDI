from models.order_detail import OrderDetailModel
from repositories.order_detail_repository import OrderDetailRepository
from schemas.order_detail_schema import OrderDetailSchema
from services.base_service_impl import BaseServiceImpl


class OrderDetailService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=OrderDetailRepository(), model=OrderDetailModel, schema=OrderDetailSchema)

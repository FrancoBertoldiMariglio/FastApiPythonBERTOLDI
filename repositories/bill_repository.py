from models.bill import BillModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import BillSchema


class BillRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(BillModel, BillSchema)

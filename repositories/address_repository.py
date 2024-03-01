from models.address import AddressModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import AddressSchema


class AddressRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(AddressModel, AddressSchema)

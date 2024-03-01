from models.address import AddressModel
from repositories.address_repository import AddressRepository
from schemas.address_schema import AddressSchema
from services.base_service_impl import BaseServiceImpl


class AddressService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=AddressRepository(), model=AddressModel, schema=AddressSchema)

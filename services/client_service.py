from models.client import ClientModel
from repositories.client_repository import ClientRepository
from schemas.client_schema import ClientSchema
from services.base_service_impl import BaseServiceImpl


class ClientService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=ClientRepository(), model=ClientModel, schema=ClientSchema)

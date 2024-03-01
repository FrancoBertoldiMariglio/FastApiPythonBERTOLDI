from models.client import ClientModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import ClientSchema


class ClientRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(ClientModel, ClientSchema)

from controllers.base_controller_impl import BaseControllerImpl
from schemas.client_schema import ClientSchema
from services.client_service import ClientService


class ClientController(BaseControllerImpl):
    def __init__(self):
        super().__init__(ClientSchema, ClientService())

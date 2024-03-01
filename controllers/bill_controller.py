from controllers.base_controller_impl import BaseControllerImpl
from schemas.bill_schema import BillSchema
from services.bill_service import BillService


class BillController(BaseControllerImpl):
    def __init__(self):
        super().__init__(BillSchema, BillService())

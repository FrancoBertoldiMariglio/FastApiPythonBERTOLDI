"""
This module provides the AddressController class which handles all operations related to addresses.
"""

from controllers.base_controller_impl import BaseControllerImpl
from schemas.address_schema import AddressSchema
from services.address_service import AddressService


class AddressController(BaseControllerImpl):
    """
    This class is a controller for the Address model. It inherits from BaseControllerImpl
    and uses AddressSchema for validation and AddressService for database operations.
    """
    def __init__(self):
        super().__init__(AddressSchema, AddressService())

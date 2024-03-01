from controllers.base_controller_impl import BaseControllerImpl
from schemas.product_schema import ProductSchema
from services.product_service import ProductService


class ProductController(BaseControllerImpl):
    def __init__(self):
        super().__init__(ProductSchema, ProductService())

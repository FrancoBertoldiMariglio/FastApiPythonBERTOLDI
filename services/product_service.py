from models.product import ProductModel
from repositories.product_repository import ProductRepository
from schemas.product_schema import ProductSchema
from services.base_service_impl import BaseServiceImpl


class ProductService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=ProductRepository(), model=ProductModel, schema=ProductSchema)

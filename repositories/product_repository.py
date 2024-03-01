from models.product import ProductModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import ProductSchema


class ProductRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(ProductModel, ProductSchema)

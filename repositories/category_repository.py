from models.category import CategoryModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import CategorySchema


class CategoryRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(CategoryModel, CategorySchema)

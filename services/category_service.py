from models.category import CategoryModel
from repositories.category_repository import CategoryRepository
from schemas.category_schema import CategorySchema
from services.base_service_impl import BaseServiceImpl


class CategoryService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=CategoryRepository(), model=CategoryModel, schema=CategorySchema)

from controllers.base_controller_impl import BaseControllerImpl
from schemas.category_schema import CategorySchema
from services.category_service import CategoryService


class CategoryController(BaseControllerImpl):
    def __init__(self):
        super().__init__(CategorySchema, CategoryService())

from models.review import ReviewModel
from repositories.review_repository import ReviewRepository
from schemas.review_schema import ReviewSchema
from services.base_service_impl import BaseServiceImpl


class ReviewService(BaseServiceImpl):

    def __init__(self):
        super().__init__(repository=ReviewRepository(), model=ReviewModel, schema=ReviewSchema)

from models.review import ReviewModel
from repositories.base_repository_impl import BaseRepositoryImpl
from schemas import ReviewSchema


class ReviewRepository(BaseRepositoryImpl):
    def __init__(self):
        super().__init__(ReviewModel, ReviewSchema)

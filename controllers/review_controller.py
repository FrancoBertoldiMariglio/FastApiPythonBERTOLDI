from controllers.base_controller_impl import BaseControllerImpl
from schemas.review_schema import ReviewSchema
from services.review_service import ReviewService


class ReviewController(BaseControllerImpl):
    def __init__(self):
        super().__init__(ReviewSchema, ReviewService())

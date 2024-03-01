from schemas.address_schema import AddressSchema
from schemas.bill_schema import BillSchema
from schemas.category_schema import CategorySchema
from schemas.client_schema import ClientSchema
from schemas.order_detail_schema import OrderDetailSchema
from schemas.order_schema import OrderSchema
from schemas.product_schema import ProductSchema
from schemas.review_schema import ReviewSchema

AddressSchema.model_rebuild()
ClientSchema.model_rebuild()
OrderSchema.model_rebuild()
ProductSchema.model_rebuild()
OrderDetailSchema.model_rebuild()
ReviewSchema.model_rebuild()
CategorySchema.model_rebuild()
BillSchema.model_rebuild()

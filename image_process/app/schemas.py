from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class ProductSchema(BaseModel):
    serial_number: int
    product_name: str
    input_image_urls: str
    output_image_urls: Optional[str] = None
    status: Optional[str] = "PENDING"

    class Config:
        orm_mode = True

class RequestSchema(BaseModel):
    request_id: UUID
    status: str

    class Config:
        orm_mode = True

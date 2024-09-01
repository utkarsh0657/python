from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
# from app.database import Base
Base = declarative_base()

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(UUID(as_uuid=True), unique=True, nullable=False)
    created_at = Column(func.now(), default=func.now())
    status = Column(String, default="PENDING")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(UUID(as_uuid=True), ForeignKey("requests.request_id"))
    serial_number = Column(Integer)
    product_name = Column(String)
    input_image_urls = Column(Text)
    output_image_urls = Column(Text, nullable=True)
    status = Column(String, default="PENDING")

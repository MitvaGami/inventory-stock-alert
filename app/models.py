from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: int
    name: str
    quantity: int
    threshold: int = Field(default=10, description="Low-stock alert triggers below this value")
    price: float

class ProductCreate(BaseModel):
    name: str
    quantity: int
    threshold: int = 10
    price: float

class ProductUpdate(BaseModel):
    quantity: Optional[int] = None
    threshold: Optional[int] = None
    price: Optional[float] = None

class Alert(BaseModel):
    product_id: int
    product_name: str
    current_quantity: int
    threshold: int
    message: str

class Report(BaseModel):
    total_products: int
    total_stock_value: float
    low_stock_count: int
    out_of_stock_count: int
    alerts: list[Alert]
    
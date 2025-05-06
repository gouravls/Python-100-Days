# order.py

from pydantic import BaseModel
from typing import List, Optional

class FoodItem(BaseModel):
    name: str
    quantity: int
    price_per_unit: float

class Order(BaseModel):
    order_id: int
    user_name: str
    items: List[FoodItem]
    address: str
    special_instruction: Optional[str] = None

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from order import OrderCalculator

router = APIRouter()

class Product(BaseModel):
    name: str
    quantity: int
    price: float

class OrderInput(BaseModel):
    customer_name: str
    products: List[Product]

@router.post("/process-order")
def process_order(order: OrderInput):
    product_dicts = [p.dict() for p in order.products]
    calc = OrderCalculator(product_dicts)

    return {
        "customer": order.customer_name,
        "total_items": calc.total_items(),
        "subtotal": calc.subtotal(),
        "tax": calc.tax(),
        "discount": calc.discount(),
        "final_amount": calc.final_amount()
    }

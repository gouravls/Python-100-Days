# main.py

from fastapi import FastAPI
from class_order_postman import Order  # Import the Order class from order.py
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.post("/submit-order")
def submit_order(order: Order):
    return {
        "message": "Order received successfully!",
        "order_summary": order
    }

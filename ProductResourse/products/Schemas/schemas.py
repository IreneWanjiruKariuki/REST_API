from pydantic import BaseModel

class ProductResponse(BaseModel):
    name: str
    description: str
    price: float
    
    class Config:
        orm_mode = True

product_data = {
    "name": "Laptop",
    "description": "A high-end gaming laptop",
    "price": 1500.00
}
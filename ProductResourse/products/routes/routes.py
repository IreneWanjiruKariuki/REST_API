from fastapi import APIRouter, HTTPException, Body
from products.Schemas.schemas import ProductsResponse

from products.Services.services import (
    get_all_products,
    add_product,
)

router = APIRouter()

@router.get("/get", response_model=list[ProductsResponse])
async def read_all_products():
    try:
        return get_all_products()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/add",response_model=ProductsResponse)
async def adding_a_product(name: str = Body(..., embed=True, title="Product Name"),
    description: str = Body(..., embed=True, title="Product Description"),
    price: float = Body(..., embed=True, title="Product Price"),):
    try:
        product= add_product(name,description,price)
        return product + HTTPException(status_code=201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
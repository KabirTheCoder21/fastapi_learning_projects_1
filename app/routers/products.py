from fastapi import *
import app.load_data.load as d
from app.utils.utils import parse_price
from app.models import *


router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/all_product")
def get_all_products():
    return d.grouped

@router.get("/price/{price_range}")
def get_products_under(price_range: float):
    result = {}

    for brand, items in d.grouped.items():
        filtered = [p for p in items if parse_price(p.price) <= price_range]
        if filtered:
            result[brand] = filtered

    return result or {"message": "No products available in this range"}

@router.get("/brand/")
def get_product_by_brand(brand:str):
    result = d.grouped.get(brand.casefold(),{})
    if not result:
        return {"msg":"This brand is not exist."}
    group = {}
    group[brand] = result
    return group
    

@router.post("/add")
def add_product(ele: dict = Body(...)):
    product = Product(**ele)
    d.products.append(product)
    brand = product.name.split()[0].casefold()
    d.grouped.setdefault(brand, []).append(product)
    return {"message": "Product added successfully", "product": product}

@router.put("/update_product")
def update_product(updated_product:dict=Body(...)):
    product = Product(**updated_product)
    print(f"updated_product : {product}")
    brand = product.name.split()[0].casefold()
    id = product.id
    brand_list = d.grouped[brand]

    for i,ele in enumerate(brand_list):
        if brand_list[i].id==id:
            brand_list[i] = product
    print(brand_list)
    d.grouped[brand] = brand_list
    print(d.grouped[brand])
    return {"msg":"product Updated",brand:brand_list}

@router.patch("/update_by_patch")
def Update_product_by_patch(update : Product):
    id = update.id
    brand = None
    existing_product = None
    for key,value in d.grouped.items():
        for product in value:
            if product.id==id:
                brand=key
                existing_product = product
                break
        if brand:
            break
    if not brand:
        return {"msg": "Product not found"}
    
    update_data = existing_product.dict()
    for key,value in update.dict().items():
        if value is not None:
            update_data[key] = value
    
    updated_product = Product(**update_data)
    for i,p in enumerate(d.grouped[brand]):
        if p.id==id:
            d.grouped[brand][i] = updated_product
            break
    return {"msg":"Succesfully updated",brand:d.grouped[brand]}



@router.delete("/delete_by_id/")
def delete_by_id(id:int):
    flag = False
    brand=None
    for key in d.grouped.keys():
        value = d.grouped[key]
        for i,p in enumerate(value):
            if p.id == id:
                brand = key
                index = i
                flag = True
                break
    if flag:
       d.grouped[brand].pop(index)
       if len(d.grouped[brand])==0:
            d.grouped.pop(brand)
       return {"msg":"Deleted Successfully."}
    return {"msg":"This id is not present."}
        

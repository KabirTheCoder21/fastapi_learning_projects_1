from pydantic import *
from typing import Dict, List

class Product(BaseModel):
    id: int
    name: str | None = None
    description: str | None = None
    price: str | None = None
    quantity: int | None = None


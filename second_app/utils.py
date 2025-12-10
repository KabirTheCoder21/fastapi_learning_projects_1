from second_app.book_mdl import *

from pydantic import ValidationError

def set_price_model_by_id(prices: list[Price], books: list[Book]) -> list[Price]:
    price_with_details = []

    for price in prices:
        for book in books:
            if price.id == book.id:
                try:
                    detail = Price(id=price.id, price=price.price, book=book)
                    #detail.price = 40 
                    price_with_details.append(detail)
                
                except ValidationError as e:
                    print(f"Validator failed for id={price.id} →", e.errors())

    return price_with_details

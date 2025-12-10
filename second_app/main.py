from fastapi import FastAPI
from pydantic import BaseModel, field_validator, ValidationError
from second_app.book_mdl import Book,Price
from second_app.utils import set_price_model_by_id

app = FastAPI()


raw_books = [
    {
        "id": 1,
        "title": "The Silent Forest",
        "author": "Lena Hart",
        "desc": "A mystery novel about a missing hiker and the secrets a small town hides.",
        "rating": 2.9
    },
    {
        "id": 2,
        "title": "Beyond the Stars",
        "author": "K. J. Rowen",
        "desc": "A sci-fi adventure following a pilot lost in deep space searching for a way home.",
        "rating": 1.8
    },
    {
        "id": 3,
        "title": "Whispers of Autumn",
        "author": "Eli Turner",
        "desc": "A romantic drama about two artists who reconnect after years apart.",
        "rating": 4.1
    },
    {
        "id": 4,
        "title": "Mathematics of the Mind",
        "author": "Dr. Ivan Kross",
        "desc": "A nonfiction exploration of cognitive science and human decision-making.",
        "rating": 4.7
    },
    {
        "id": 5,
        "title": "Shadows of the Empire",
        "author": "Marcel Yun",
        "desc": "A political thriller set in a fictional kingdom where betrayal fuels a civil war.",
        "rating": 4.4
    },
    {
        "id": 6,
        "title": "Cooking with Color",
        "author": "Amara Fields",
        "desc": "A vibrant cookbook focused on healthy recipes organized by color groups.",
        "rating": "4.8"
    },
    {
        "id": 7,
        "title": "Rust & Rain",
        "author": "J. M. Calder",
        "desc": "A gritty cyberpunk noir about a detective solving crimes in a megacity.",
        "rating": 4.5
    },
    {
        "id": 8,
        "title": "The Last Garden",
        "author": "Sarah Reeves",
        "desc": "A post-apocalyptic tale where a young botanist discovers the key to restoring Earth.",
        "rating": 4.2
    },
    {
        "id": 9,
        "title": "Ocean Bones",
        "author": "Tao Ridge",
        "desc": "A deep-sea horror story involving a lost submarine and ancient underwater creatures.",
        "rating": "four"
    },
    {
        "id": 10,
        "title": "Patterns of Power",
        "author": "Nadia Serrano",
        "desc": "A business and leadership book analyzing influence structures in organizations.",
        "rating": 4.6
    }
]

# raw_price =[
# {
#     'id':1,
#     'price':21.90
# },
# {
#     'id':3,
#     'price':"31.90"
# },
# {
#     'id':5,
#     'price':51.90
# }
# ] 
# prices = []
# for price in raw_price:
#     prices.append(Price.model_validate(price))

Books = []
for rb in raw_books:
    try:
        Books.append(Book.model_validate(rb))
    except ValidationError as e:
        print("Validation error →", e.errors())

sample_price_data = [
    {
        "id": 1, 
        "price": 79.99,
    },
    {
        "id": 2, 
        "price": "34.50",
    },
    {
        "id": 3, 
        "price": 69.99
    },
    {
        "id": 4, 
        "price": 12.00
    },
    {
        "id": 5, 
        "price": 35
    }
]

prices=[]
for price in sample_price_data:
    try:
        prices.append(Price(id = price["id"],price=price["price"]))
    except ValidationError as e:
        print("Validation error →", e.errors())
prices_with_extra_details = set_price_model_by_id(prices,Books)


@app.get("/books/ratings/")
def get_all_details_by_rating(rating: float):
    result = []

    for details in prices_with_extra_details:
        if not details.book:
            continue
        if details.book.rating >= rating:
            result.append(details)

    if not result:
        return {"msg": "No books available for the given rating."}
    
    return {
        "size": len(result),
        "result": result
    }



@app.get("/books")
def read_books():
    return {"size" : len(Books), "books": Books}

@app.get("/books/price_details")
def get_price_with_extra_details():
    return prices_with_extra_details

# @app.get("/book_price/")
# def get_price_by_id(id:int):
#     for price in prices:
#         if id == price.id:
#             return {"id":id,'price':price.price}
#     return {"msg":f"Price is not fixed for this id : {id}"}



from fastapi import  Body, FastAPI
from typing import List
from pydantic import ValidationError
from user_management.models.user import User, UserResponseInvalid, UserResponseItem, UserResponseValid, UsersResponse

app = FastAPI()

users_data = [
    {"name": "Rohan", "age": 21, "email": None, "password": "123456", "confirm_password": "123456"},
    {"name": "Alex", "age": 19, "email": "alex@example.com", "password": "abcdef", "confirm_password": "abcdef"},
    {"name": "John", "age": 25, "email": "john@example.com", "password": "654321", "confirm_password": "654321"}
]

@app.get("/users", response_model=UsersResponse)
def get_users():
    results: List[UserResponseItem] = []

    for index, data in enumerate(users_data):
        try:
            user = User(**data)
            results.append(UserResponseValid(index=index,user=user))
        except ValidationError as e:
            results.append(UserResponseInvalid(
                index=index,
                errors=[err["msg"] for err in e.errors()]
            ))

    return {
        "size":len(users_data),
        "data":results
    }
@app.post("/create_user")
def create_user(body:dict=Body(...,example={
            "name": "Sohan",
            "age": 22,
            "email": None,
            "password": "123457",
            "confirm_password": "123457"
        }
    )):
    try:
        user = User(**body)
        users_data.append(user.model_dump())
        return {"msg":"Successfully user created."}
    except ValidationError as e:
        return {"errors": [err["msg"] for err in e.errors()]}

@app.patch("/update_user")
def update_user(user: User):
    updated_fields = user.model_dump(exclude_unset=True)

    identifier = updated_fields.get("email")
    if not identifier:
        return {"error": "Email is required to update user"}

    for i, existing_user in enumerate(users_data):
        if existing_user.get("email") == identifier:

            users_data[i].update(updated_fields)

            return {"msg": "Successfully updated."}

    return {"error": "User not found"}

@app.patch("/add_email")
def add_mail(detail:User):
    updated_fields = detail.model_dump(exclude_unset=True)
    for i,existing_user in enumerate(users_data):
        if existing_user.get("name",None)==updated_fields.get("name",None):
            users_data[i].update(updated_fields)
            return {"msg: Successfully added."}
    return {"msg:Something went wrong."}

from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator, model_validator

class User(BaseModel):
    name: str = Field(default=None, min_length=4, example="Raja Ji")
    age: int = Field(default = None, ge=18, example=18)
    email: Optional[EmailStr] |None = None
    password: str = Field(..., min_length=6)
    confirm_password: str = Field(..., min_length=6)

    @field_validator("name", mode="after")
    def check_name(cls, v):
        if not v.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters.")
        return v

    @field_validator("age", mode="after")
    def check_age(cls, v):
        if v < 18:
            raise ValueError("Age must be greater than 18.")
        return v

    @model_validator(mode="after")
    def match_passwords(cls, data):
        if data.password != data.confirm_password:
            raise ValueError("Password and Confirm Password must match.")
        return data

class UserResponseValid(BaseModel):
    index: int
    status: str = "valid"
    user: User

class UserResponseInvalid(BaseModel):
    index: int
    status: str = "invalid"
    errors: List[str]

UserResponseItem = Union[UserResponseValid, UserResponseInvalid]

class UsersResponse(BaseModel):
    size: int
    data: List[UserResponseItem]

class User2(BaseModel):
    name:str
    is_valid:bool
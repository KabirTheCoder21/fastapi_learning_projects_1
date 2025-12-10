from pydantic import BaseModel, ValidationInfo, field_validator, model_validator

class Book(BaseModel):
    id: int
    title: str | None = None
    author: str | None = None
    desc: str | None = None
    rating: float | None = None

    @field_validator("rating", mode="before")
    def validate_rating(cls, v):
        if v is None:
            return None
        
        if isinstance(v, (int, float)):
            if v <= 5.0:
                return float(v)
            else:
                raise ValueError("rating must be <= 5.0")
        
        if isinstance(v, str):
            v = v.strip()
            try:
                rating_float = float(v)
                if rating_float <= 5.0:
                    return rating_float
                else:
                    raise ValueError("rating must be <= 5.0")
            except ValueError:
                raise ValueError(f"rating must be numeric, got {v!r}")
        raise TypeError("rating must be a number or numeric string")

# class Price(Book):
#     price: float


class Price(BaseModel):
    id:int
    price: float
    book:Book | None = None

    model_config = {"validate_assignment": True}

    @model_validator(mode="after")
    def check_price_based_on_rating(self):
        if self.book and self.book.rating is not None:
            if self.book.rating < 3 and self.price > 50:
                raise ValueError("Low-rated books cannot have high prices")
        return self   

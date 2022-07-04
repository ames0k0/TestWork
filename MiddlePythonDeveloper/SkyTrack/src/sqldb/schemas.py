from pydantic import BaseModel


class BookBody(BaseModel):
    id: int
    shop_id: int
    quantity: int


class OrderItem(BaseModel):
    books: list[BookBody]

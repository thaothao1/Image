from pydantic import BaseModel

class ItemBase(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True


from http.client import HTTPException
from fastapi import APIRouter , status
from typing import List
from models.database import SessionLocal
from models import Items
from pydantic import BaseModel


app = APIRouter()


class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode=True

db=SessionLocal()

@app.get('/items', response_model = List[Item], status_code  = 200)
def get_all_items():
    items= db.query(Items.Item).all()
    return items


@app.post('/items', response_model=Item ,status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item= db.query(Items.Item).filter(Items.Item.name == item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=400 , detail="Item already exists")
    
    new_item= Items.Item(
        name= item.name,
        price= item.price,
        description = item.description,
        on_offer = item.on_offer
    )

    db.add(new_item)
    db.commit()

    return new_item



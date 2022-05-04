from http.client import HTTPException
from inspect import CORO_SUSPENDED
from urllib import response
from fastapi import APIRouter , status , File , FastAPI
from typing import List
from models.database import SessionLocal
from models.PhotoBase import PhotoModel

from PIL import Image
import io

app= APIRouter()
# app = FastAPI()
db= SessionLocal()

# @router.get('/photos', response_model = List[])


@app.get("/")
async def root():
    return {"meassage" : "hello"}

@app.post("/upload")
async def recieveFile(file: bytes= File(...)):
    image = Image.open(io.BytesIO(file))
    image.show()
    print(image)
    return {"uploadstatus" : "complete"}

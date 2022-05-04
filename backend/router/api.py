from fastapi import APIRouter
from router import action , Img

router = APIRouter()
router.include_router(action.app, tags=['actions'] , prefix ="/action")
router.include_router(Img.app, tags=['imgs'] , prefix ="/img")
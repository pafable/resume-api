from fastapi import APIRouter
from .mydata import EDU_DATA

router = APIRouter()

@router.get("/")
async def education() -> dict:
    return EDU_DATA
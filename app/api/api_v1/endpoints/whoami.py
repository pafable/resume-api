from fastapi import APIRouter
from .mydata import ME

router = APIRouter()

@router.get("/")
async def whoami() -> dict:
    return ME

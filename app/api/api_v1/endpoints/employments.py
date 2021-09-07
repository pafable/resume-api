from fastapi import APIRouter
from .mydata import JOBS_DATA

router = APIRouter()

@router.get("/")
async def employments() -> dict:
    return JOBS_DATA
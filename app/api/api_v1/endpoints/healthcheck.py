from fastapi import APIRouter, HTTPException
import sys

OSCHECK = sys.platform

router = APIRouter()

@router.get("/")
async def healthcheck() -> dict:
    if OSCHECK == "linux":
        x = {"status": "ok", "platform": OSCHECK}
    else:   
        x = {"status": "not ok", "platform": OSCHECK}
        raise HTTPException(status_code=500, detail="Not running on linux!")
    
    return x
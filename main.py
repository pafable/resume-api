from typing import Optional
from mydata import JOBS_DATA, EDU_DATA
from fastapi import FastAPI, HTTPException, status
from starlette.responses import RedirectResponse
from pydantic import BaseModel
import sys

OSCHECK = sys.platform

class Employment(BaseModel):
    employer: str
    title: str
    location: str
    start_date: str
    end_date: str
    intern: Optional[bool] = None
    contractor: Optional[bool] = None


class Schools(BaseModel):
    school: str
    degree: str   


app = FastAPI()

@app.get("/")
async def index() -> str:
    return RedirectResponse(url="/docs")


@app.get("/healthcheck")
async def healthcheck() -> dict:
    if OSCHECK == "linux":
        x = {"status": "ok", "platform": OSCHECK}
    else:   
        x = {"status": "not ok", "platform": OSCHECK}
        raise HTTPException(status_code=500, detail="Not running on linux!")
    
    return x


@app.get("/employments")
async def employments() -> dict:
    return JOBS_DATA

@app.get("/education")
async def education() -> dict:
    return EDU_DATA
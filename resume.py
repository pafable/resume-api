from typing import Optional
from fastapi import FastAPI, HTTPException, status
from starlette.responses import RedirectResponse
from pydantic import BaseModel
import datetime
import sys

OSCHECK = sys.platform

def employment_date(year: int, month: int) -> str:
    z = datetime.date(year, month, 1)
    z = z.strftime("%B %Y")

    return z


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


JOBS_DATA = {

    "jobs": [
        {         
            "employer": "Sophos", 
            "title": "Systems Engineer", 
            "location": "Burlington, MA",
            "start_date": employment_date(2019, 4), 
            "end_date": None,
            "intern": False,
            "contractor": False
        },
        {         
            "employer": "PTC", 
            "title": "Cloud Engineer", 
            "location": "Needham, MA",
            "start_date": employment_date(2017, 1), 
            "end_date": employment_date(2019, 4),
            "intern": False,
            "contractor": False
        },
        {         
            "employer": "NWN", 
            "title": "Solutions Engineer", 
            "location": "Waltham, MA",
            "start_date": employment_date(2015, 7), 
            "end_date": employment_date(2016, 12),
            "intern": False,
            "contractor": False
        },
        {        
            "employer": "EMC", 
            "title": "Network Operation Intern", 
            "location": "Southborough, MA",
            "start_date": employment_date(2015, 2), 
            "end_date": employment_date(2015, 6),
            "intern": True,
            "contractor": False
        },  
        {
            "employer": "Suffolk Construction", 
            "title": "Business Systems Intern", 
            "location": "Boston, MA",
            "start_date": employment_date(2014, 9), 
            "end_date": employment_date(2015, 1),
            "intern": True,
            "contractor": False
        }
    ]

}


EDU_DATA = {

    "education": [
        {
            "school": "Western Governor's University",
            "degree": "BS, Information Technology",
        },
        {
            "school": "Bunker Hill Community College",
            "degree": "AS, Computer Information Technology"
        }
    ] 

}


app = FastAPI()

@app.get("/")
async def index() -> str:
    return RedirectResponse(url="/docs")


@app.get("/healthcheck")
def healthcheck() -> dict:
    if OSCHECK == "linux":
        x = {"status": "ok", "platform": OSCHECK}
    else:   
        x = {"status": "not ok", "platform": OSCHECK}
        raise HTTPException(status_code=500, detail="Not running on linux!")
    
    return x


@app.get("/employments")
def employments() -> dict:
    return JOBS_DATA

@app.get("/education")
def education() -> dict:
    return EDU_DATA
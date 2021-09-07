from fastapi import FastAPI
from app.api.api_v1.api import router as api_router
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def index() -> str:
    return RedirectResponse(url="/api/v1/whoami")

app.include_router(api_router, prefix="/api/v1")
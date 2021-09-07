from fastapi import APIRouter
from .endpoints import employments, education, healthcheck, whoami

router = APIRouter()

router.include_router(employments.router, prefix="/employments", tags=["Job History"])
router.include_router(education.router, prefix="/education", tags=["Education History"])
router.include_router(healthcheck.router, prefix="/healthcheck", tags=["Healthcheck"])
router.include_router(whoami.router, prefix="/whoami", tags=["Me"])
from fastapi import FastAPI

from app.config import settings

from app.routers.ingest import router as ingest_router
from app.routers.dashboard import router as dashboard_router
from app.routers.ai import router as ai_router

app = FastAPI(
    title=settings.project_name,
    version="1.0.0",
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "application": settings.project_name,
    }


app.include_router(
    ingest_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    ai_router
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from core.database import engine, Base
from api.endpoints import router as api_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="STVRAF Framework API",
    description="Sovereign Threat Vector Risk Assessment Framework (STVRAF) Backend API",
    version="1.0.0"
)


# Configure CORS (allow all for research purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include the API router
app.include_router(api_router, prefix="/api/v1")


# Mount static files directory if it exists
if os.path.exists("public"):
    app.mount("/static", StaticFiles(directory="public"), name="static")


@app.get("/")
def read_root():
    """Serve the HTML landing page."""
    if os.path.exists("public/index.html"):
        return FileResponse("public/index.html")

    return {"message": "Welcome to the STVRAF Framework API"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from core.database import engine, Base
from core.custom_docs import get_swagger_ui_html_with_analytics, get_redoc_html_with_analytics
from api.endpoints import router as api_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="STVRAF Framework API",
    description="Sovereign Threat Vector Risk Assessment Framework (STVRAF) Backend API",
    version="1.0.0",
    docs_url=None,  # Disable default docs to use custom ones with analytics
    redoc_url=None  # Disable default redoc to use custom one with analytics
)

# Configure CORS (allow all for research purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/", response_class=FileResponse)
def read_root():
    """Serve the main landing page with Vercel Web Analytics"""
    return FileResponse("static/index.html")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom Swagger UI with Vercel Web Analytics"""
    return get_swagger_ui_html_with_analytics(
        openapi_url=app.openapi_url,
        title=f"{app.title} - Swagger UI",
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """Custom ReDoc with Vercel Web Analytics"""
    return get_redoc_html_with_analytics(
        openapi_url=app.openapi_url,
        title=f"{app.title} - ReDoc",
    )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

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

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>STVRAF Framework API</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #0070f3;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            font-size: 1.1em;
            margin-bottom: 30px;
        }
        .links {
            display: flex;
            gap: 20px;
            margin: 30px 0;
        }
        .link-button {
            display: inline-block;
            padding: 12px 24px;
            background-color: #0070f3;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.2s;
        }
        .link-button:hover {
            background-color: #0051cc;
        }
        .endpoints {
            margin-top: 40px;
        }
        .endpoint {
            background-color: #f5f5f5;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-left: 4px solid #0070f3;
        }
        .method {
            font-weight: bold;
            color: #0070f3;
            margin-right: 10px;
        }
    </style>
    <!-- Vercel Speed Insights -->
    <script>
      window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
</head>
<body>
    <h1>STVRAF Framework API</h1>
    <p class="subtitle">Sovereign Threat Vector Risk Assessment Framework</p>
    
    <p>A production-grade REST API backend implementing the STVRAF research framework — a Bayesian probabilistic model for assessing and tracking cyber-physical risk across fleet segments.</p>
    
    <div class="links">
        <a href="/docs" class="link-button">API Documentation (Swagger)</a>
        <a href="/redoc" class="link-button">API Documentation (ReDoc)</a>
    </div>
    
    <div class="endpoints">
        <h2>Available Endpoints</h2>
        <div class="endpoint">
            <span class="method">POST</span><code>/api/v1/segments/</code> - Create fleet segment
        </div>
        <div class="endpoint">
            <span class="method">GET</span><code>/api/v1/segments/{id}</code> - Get risk score
        </div>
        <div class="endpoint">
            <span class="method">POST</span><code>/api/v1/telemetry/</code> - Ingest telemetry & update risk
        </div>
    </div>
</body>
</html>
    """

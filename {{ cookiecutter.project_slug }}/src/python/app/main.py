# src/python/app/main.py

from fastapi import FastAPI
from app.api.v1.routers.health import router as health_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url=None,
    swagger_ui_parameters={
        "docExpansion": "none",   
        "defaultModelsExpandDepth": -1, 
        "displayRequestDuration": True,  
    },
    openapi_tags=[  
        {
            "name": "Ping",
            "description": "Lightweight endpoint consumed by orchestrators (K8s, Nomad, …) to check container liveness/readiness.",
        }
    ],
)

app.include_router(health_router)

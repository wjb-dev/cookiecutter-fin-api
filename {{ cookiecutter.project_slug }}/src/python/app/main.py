from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api.v1.routers.health import router as health_router
from app.core.config import settings
from typing import Dict, Any

tags_metadata = [
        {
            "name": "Ping",
            "description": "Lightweight endpoint consumed by orchestrators (K8s, Nomad, …) to check container liveness/readiness.",
        }
    ]

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
    openapi_tags= tags_metadata
)
def _custom_openapi() -> Dict[str, Any]:
    if app.openapi_schema:  # cache
        return app.openapi_schema

    schema = get_openapi(
        title=settings.app_name,
        version=settings.version,
        description=settings.description,
        routes=app.routes,
    )
    schema["tags"] = tags_metadata
    schema["info"].update(
        {
            "contact": {
                "name": "WJB-DEV",
                "url": "https://github.com/wjb-dev",
                "email": "support@example.com",
            },
            "license": {
                "name": "MIT",
                "url": "https://opensource.org/licenses/MIT",
            },
        }
    )
    schema["servers"] = [{"url": "/", "description": "default"}]
    app.openapi_schema = schema
    return schema


app.openapi = _custom_openapi  # monkey-patch the generator
app.include_router(health_router)

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from src.app.api.v1.routers.health import router as health_router
from src.app.core.config import settings
from typing import Dict, 

logger = logging.getLogger("uvicorn.info")

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
    if app.openapi_schema:
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


app.openapi = _custom_openapi
app.include_router(health_router)

@app.on_event("startup")
async def _print_swagger_banner():
    """
    When the app starts, log a neat box with the Local and (if resolvable) Network URLs
    pointing at your Swagger UI (e.g. docs_url).
    """
    port = settings.port
    docs_path = app.docs_url or "/docs"
    local_url = f"http://localhost:{port}{docs_path}"

    try:
        host = socket.gethostbyname(socket.gethostname())
        network_url = f"http://{host}:{port}{docs_path}"
        show_network = host not in ("127.0.0.1", "localhost")
    except Exception:
        network_url = ""
        show_network = False

    logger,info(f"✅  Swagger UI available at: {local_url}")
    logger,info(f"✅  Swagger UI available at: {network_url}")


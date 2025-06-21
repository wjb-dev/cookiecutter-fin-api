from src.app.core.config import settings

def get_health() -> dict:
    return {
        "service": settings.app_name,
        "status": "ok",
        "version": settings.version,
    }
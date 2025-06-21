from pydantic import BaseModel

class HealthResponse(BaseModel):
    service: str
    status: str
    version: str

    class Config:
        schema_extra = {
            "example": {
                "service": "{{ cookiecutter.project_slug }}",
                "status": "ok",
                "version": "0.1.0",
            }
        }

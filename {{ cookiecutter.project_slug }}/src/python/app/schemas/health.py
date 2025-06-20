from pydantic import BaseModel

class HealthResponse(BaseModel):
    service: str
    status: str
    version: str

    class Config:
        schema_extra = {
            "example": {
                "service": "options-greeks-api",
                "status": "ok",
                "version": "0.1.0",
            }
        }

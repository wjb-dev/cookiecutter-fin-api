from app.schemas.health import HealthResponse
import pytest
import json

def test_health_response_model():
    data = {"service":"options-greeks-api","status":"ok","version":"0.1.0"}
    model = HealthResponse(**data)
    assert model.service == "options-greeks-api"
    assert model.status == "ok"
    assert model.version == "0.1.0"

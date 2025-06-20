import pytest
from fastapi import status
from app.api.v1.routers.health import healthz

def test_healthz_return_value(monkeypatch):
    # If you had any dependencies (e.g. a service), monkeypatch them here.
    response = healthz()
    assert response.status_code == status.HTTP_200_OK
    body = response.body.decode()
    assert '"service":' in body
    assert '"status":"ok"' in body

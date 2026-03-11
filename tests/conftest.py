import pytest
from fastapi.testclient import TestClient

from app import database as db
from app.main import app


@pytest.fixture
def client():
    db.reset_database()
    with TestClient(app) as c:
        yield c
    db.reset_database()

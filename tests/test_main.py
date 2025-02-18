from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, engine
from app.models import Base

client = TestClient(app)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_create_log():
    response = client.post(
        "/logs/",
        json={"timestamp": "2023-10-01T12:00:00Z", "level": "INFO", "message": "Test", "source": "test"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Log recebido com sucesso!"

def test_read_logs():
    response = client.get("/logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

# Set up test client
client = TestClient(app)

# Set up and tear down the test database
@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    # Recreate tables before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Optional: cleanup afterward
    Base.metadata.drop_all(bind=engine)

def test_register_user():
    response = client.post("/api/users/", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

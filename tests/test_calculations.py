import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_calculation():
    payload = {
        "operation": "add",
        "operand1": 10.0,
        "operand2": 5.0,
        "result": 15.0
    }
    response = client.post("/api/calculations/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["operation"] == "add"
    assert data["result"] == 15.0
    assert "id" in data

def test_get_all_calculations():
    client.post("/api/calculations/", json={
        "operation": "multiply",
        "operand1": 3.0,
        "operand2": 4.0,
        "result": 12.0
    })
    response = client.get("/api/calculations/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(item["operation"] == "multiply" for item in data)

def test_get_single_calculation():
    post_resp = client.post("/api/calculations/", json={
        "operation": "divide",
        "operand1": 20.0,
        "operand2": 4.0,
        "result": 5.0
    })
    calc_id = post_resp.json()["id"]

    get_resp = client.get(f"/api/calculations/{calc_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["operation"] == "divide"

def test_update_calculation():
    post_resp = client.post("/api/calculations/", json={
        "operation": "subtract",
        "operand1": 9.0,
        "operand2": 2.0,
        "result": 7.0
    })
    calc_id = post_resp.json()["id"]

    updated_data = {
        "operation": "subtract",
        "operand1": 9.0,
        "operand2": 4.0,
        "result": 5.0
    }
    put_resp = client.put(f"/api/calculations/{calc_id}", json=updated_data)
    assert put_resp.status_code == 200
    assert put_resp.json()["result"] == 5.0

def test_delete_calculation():
    post_resp = client.post("/api/calculations/", json={
        "operation": "power",
        "operand1": 2.0,
        "operand2": 3.0,
        "result": 8.0
    })
    calc_id = post_resp.json()["id"]

    del_resp = client.delete(f"/api/calculations/{calc_id}")
    assert del_resp.status_code == 200
    assert del_resp.json()["detail"] == "Calculation deleted"

    # Confirm it’s gone
    get_resp = client.get(f"/api/calculations/{calc_id}")
    assert get_resp.status_code == 404

def test_get_invalid_calculation():
    response = client.get("/api/calculations/9999")
    assert response.status_code == 404

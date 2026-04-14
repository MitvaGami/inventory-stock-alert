from fastapi.testclient import TestClient
from app.main import app, products_db

client = TestClient(app)


def setup_function():
    products_db.clear()  # reset before each test


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_add_product():
    response = client.post("/products", json={
        "name": "Test Product",
        "quantity": 5,
        "threshold": 10,
        "price": 100.0
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Test Product"


def test_get_products():
    client.post("/products", json={
        "name": "A",
        "quantity": 5,
        "threshold": 10,
        "price": 100
    })
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_update_product():
    res = client.post("/products", json={
        "name": "A",
        "quantity": 5,
        "threshold": 10,
        "price": 100
    })
    pid = res.json()["id"]

    response = client.put(f"/products/{pid}", json={"quantity": 20})
    assert response.status_code == 200
    assert response.json()["quantity"] == 20


def test_delete_product():
    res = client.post("/products", json={
        "name": "A",
        "quantity": 5,
        "threshold": 10,
        "price": 100
    })
    pid = res.json()["id"]

    response = client.delete(f"/products/{pid}")
    assert response.status_code == 200
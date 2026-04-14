from fastapi import FastAPI, HTTPException
from app.models import Product, ProductCreate, ProductUpdate, Alert
from app.alerts import check_alerts, generate_report

app = FastAPI(
    title="Inventory & Stock Alert System",
    description="Tracks product inventory, triggers low-stock alerts, and generates reports.",
    version="1.0.0"
)

# In-memory store (acts as our database for this project)
products_db: dict[int, Product] = {}
_id_counter = 1  # auto-increment ID


# ── Seed data so the app is useful on first run ──────────────────────────────
def seed_data():
    global _id_counter
    seeds = [
        ProductCreate(name="Wireless Mouse",    quantity=3,  threshold=10, price=599.0),
        ProductCreate(name="USB-C Hub",         quantity=15, threshold=10, price=1299.0),
        ProductCreate(name="Mechanical Keyboard",quantity=0, threshold=5,  price=2499.0),
        ProductCreate(name="Monitor Stand",     quantity=8,  threshold=10, price=899.0),
        ProductCreate(name="Webcam HD",         quantity=20, threshold=10, price=3499.0),
    ]
    for s in seeds:
        global _id_counter
        products_db[_id_counter] = Product(id=_id_counter, **s.model_dump())
        _id_counter += 1

seed_data()


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    return {"status": "running", "service": "Inventory & Stock Alert System"}


@app.get("/products", response_model=list[Product], tags=["Products"])
def get_all_products():
    """Returns all products in the inventory."""
    return list(products_db.values())


@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int):
    """Returns a single product by ID."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return products_db[product_id]


@app.post("/products", response_model=Product, status_code=201, tags=["Products"])
def add_product(product: ProductCreate):
    """Adds a new product to the inventory."""
    global _id_counter
    new_product = Product(id=_id_counter, **product.model_dump())
    products_db[_id_counter] = new_product
    _id_counter += 1
    return new_product


@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def update_product(product_id: int, updates: ProductUpdate):
    """Updates stock quantity, threshold, or price of an existing product."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    existing = products_db[product_id]
    updated_data = existing.model_dump()
    for field, value in updates.model_dump(exclude_none=True).items():
        updated_data[field] = value
    products_db[product_id] = Product(**updated_data)
    return products_db[product_id]


@app.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: int):
    """Removes a product from the inventory."""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    deleted = products_db.pop(product_id)
    return {"message": f"Product '{deleted.name}' deleted successfully"}


@app.get("/alerts", response_model=list[Alert], tags=["Alerts"])
def get_alerts():
    """Returns all products currently below their stock threshold."""
    return check_alerts(products_db)


@app.get("/report", tags=["Reports"])
def get_report():
    """Generates a full inventory summary report with alert details."""
    return generate_report(products_db)
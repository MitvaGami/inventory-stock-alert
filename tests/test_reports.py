from app.alerts import generate_report
from app.models import Product


def test_generate_report():
    products = {
        1: Product(id=1, name="A", quantity=2, threshold=5, price=100),
        2: Product(id=2, name="B", quantity=10, threshold=5, price=200),
    }

    report = generate_report(products)

    assert report["total_products"] == 2
    assert report["low_stock_count"] == 1
    assert report["out_of_stock_count"] == 0
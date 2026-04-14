from app.alerts import check_alerts
from app.models import Product


def test_check_alerts():
    products = {
        1: Product(id=1, name="A", quantity=2, threshold=5, price=100),
        2: Product(id=2, name="B", quantity=10, threshold=5, price=200),
        3: Product(id=3, name="C", quantity=0, threshold=5, price=300),
    }

    alerts = check_alerts(products)

    assert len(alerts) == 2
    assert any(a.product_name == "A" for a in alerts)
    assert any(a.product_name == "C" for a in alerts)
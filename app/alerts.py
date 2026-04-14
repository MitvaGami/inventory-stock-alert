from app.models import Product, Alert

def check_alerts(products: dict[int, Product]) -> list[Alert]:
    """
    Core business logic — triggers an alert for every product
    whose quantity is below its configured threshold.
    """
    alerts = []
    for product in products.values():
        if product.quantity < product.threshold:
            if product.quantity == 0:
                message = f"CRITICAL: '{product.name}' is completely out of stock!"
            else:
                message = (
                    f"LOW STOCK: '{product.name}' has only {product.quantity} units "
                    f"left (threshold: {product.threshold})."
                )
            alerts.append(Alert(
                product_id=product.id,
                product_name=product.name,
                current_quantity=product.quantity,
                threshold=product.threshold,
                message=message
            ))
    return alerts


def generate_report(products: dict[int, Product]) -> dict:
    """
    Generates a full inventory summary report.
    """
    alerts = check_alerts(products)
    total_value = sum(p.quantity * p.price for p in products.values())
    out_of_stock = [p for p in products.values() if p.quantity == 0]

    return {
        "total_products": len(products),
        "total_stock_value": round(total_value, 2),
        "low_stock_count": len(alerts),
        "out_of_stock_count": len(out_of_stock),
        "alerts": alerts
    }
# app/services/stock_service.py
from app.models import Product
from app import db

def validate_and_deduct_stock(products):
    total_price = 0
    updated_products = []

    for item in products:
        product = Product.query.get(item['id'])
        if not product:
            raise ValueError(f"Product with ID {item['id']} not found.")

        if product.stock < item['quantity']:
            raise ValueError(f"Insufficient stock for product ID {item['id']}.")

        product.stock -= item['quantity']
        total_price += product.price * item['quantity']
        updated_products.append({
            'id': product.id,
            'quantity': item['quantity'],
            'price': product.price
        })

    db.session.commit()
    return total_price, updated_products
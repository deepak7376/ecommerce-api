# app/routes/orders.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Order
from app.services.stock_service import validate_and_deduct_stock

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('', methods=['POST'])
def place_order():
    data = request.get_json()
    if not data or 'products' not in data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        products = data['products']  # List of {'id': product_id, 'quantity': quantity}
        total_price, updated_products = validate_and_deduct_stock(products)

        new_order = Order(
            products=updated_products,
            total_price=total_price,
            status='pending'
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order placed successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
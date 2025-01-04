# app/routes/products.py
from flask import Blueprint, request, jsonify
from app.models import Product
from app.utils.exceptions import ProductNotFoundError
from app import db

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'stock': product.stock
    } for product in products]
    return jsonify(product_list), 200

@products_bp.route('', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        new_product = Product(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify({"message": "Product added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a product by ID"""
    try:
        product = Product.query.get(product_id)
        print(product)
        if product is None:
            raise ProductNotFoundError("Product not found!")
        return jsonify(product.to_dict())
    except ProductNotFoundError as e:
        return jsonify({'error': str(e)}), 404
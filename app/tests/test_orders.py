import pytest
from app import create_app, db
from app.models import Order, Product
from app.services.stock_service import update_stock


@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()
    yield app
    db.drop_all()
    
@pytest.fixture
def new_order():
    order = Order(user_id=1, total_price=50.0)
    return order

@pytest.fixture
def new_product():
    product = Product(name='Test Product', price=10.0, stock=100)
    return product

def test_create_order(app, new_order, new_product):
    """Test creating a new order"""
    with app.app_context():
        db.session.add(new_product)
        db.session.add(new_order)
        db.session.commit()
        order = Order.query.get(new_order.id)
        assert order is not None
        assert order.total_price == 50.0

def test_order_stock_update(app, new_order, new_product):
    """Test stock update after an order is placed"""
    with app.app_context():
        db.session.add(new_product)
        db.session.add(new_order)
        db.session.commit()
        update_stock(new_order, new_product)
        product = Product.query.get(new_product.id)
        assert product.stock == 99  # assuming stock is reduced after an order

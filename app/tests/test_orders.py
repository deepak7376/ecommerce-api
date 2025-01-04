import pytest
from app import create_app, db
from app.models import Order, Product
import config


@pytest.fixture
def app():
    app = create_app(config_class=config.TestConfig)
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


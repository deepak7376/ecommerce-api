import pytest
from app import create_app, db
from app.models import Product

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()
    yield app
    db.drop_all()

@pytest.fixture
def new_product():
    product = Product(name='Test Product', price=10.0, stock=100)
    return product

def test_create_product(app, new_product):
    """Test creating a new product"""
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        assert new_product.id is not None
        assert new_product.name == 'Test Product'

def test_get_product(app, new_product):
    """Test getting a product by id"""
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        product = Product.query.get(new_product.id)
        assert product is not None
        assert product.name == 'Test Product'

def test_get_product_not_found(app):
    """Test case for a product that doesn't exist"""
    with app.app_context():
        product = Product.query.get(999)
        assert product is None

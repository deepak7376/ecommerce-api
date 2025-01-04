from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class='config.Config'):
    """Application Factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    print(app.config)
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.products import products_bp
    from app.routes.orders import orders_bp
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app

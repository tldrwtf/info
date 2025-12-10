from flask import Flask
from .models import db
from .extensions import ma, limiter, cache
from .blueprints.user import users_bp
from .blueprints.books import books_bp
from .blueprints.loans import loans_bp
from .blueprints.orders import orders_bp
from .blueprints.items import items_bp
from flask_swagger_ui import get_swaggerui_blueprint #need to create a blueprint to plug into our app

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Library API"
    }
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    # Import routes here to avoid circular imports and ensure routes are registered
    # when the app is created.
    from .blueprints.user import routes as user_routes
    from .blueprints.books import routes as books_routes
    from .blueprints.loans import routes as loans_routes
    from .blueprints.orders import routes as orders_routes
    from .blueprints.items import routes as items_routes
    
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(books_bp, url_prefix='/books')
    app.register_blueprint(loans_bp, url_prefix='/loans')
    app.register_blueprint(orders_bp, url_prefix='/orders')
    app.register_blueprint(items_bp, url_prefix='/items')
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
from flask import Flask
from .models import db
from .extensions import ma, limiter, cache
from .blueprints.user import users_bp
from .blueprints.books import books_bp
from .blueprints.loans import loans_bp

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(f'config.{config_name}')

  # Initialize my extension onto my Flask app
  db.init_app(app) #adding the db to the app
  ma.init_app(app)
  limiter.init_app(app)
  cache.init_app(app)

  #Register blueprints
  app.register_blueprint(users_bp, url_prefix='/users')
  app.register_blueprint(books_bp, url_prefix='/books')
  app.register_blueprint(loans_bp, url_prefix='/loans')

  return app
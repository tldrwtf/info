class DevelopmentConfig:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
  DEBUG = True
  CACHE_TYPE = "SimpleCache"
  CACHE_DEFAULT_TIMEOUT = 300

class TestingConfig:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
  TESTING = True
  DEBUG = False
  CACHE_TYPE = "NullCache"
  CACHE_DEFAULT_TIMEOUT = 0

class ProductionConfig:
  SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'
  DEBUG = False
  CACHE_TYPE = "SimpleCache"
  CACHE_DEFAULT_TIMEOUT = 600

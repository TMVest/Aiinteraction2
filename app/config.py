import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me-before-deploying-anywhere-real")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "instance", "computersai.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    WTF_CSRF_ENABLED = False

class ProdConfig(Config):
    DEBUG = False

    @staticmethod
    def init_app(app):
        # enforce that real secrets are set in production
        app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

config_by_name = {
    "development": Config,
    "testing": TestConfig,
    "production": ProdConfig,
}
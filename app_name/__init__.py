from flask import Flask

from app_name.assets import load_assets
from app_name.routes import add_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('tracking_page.config.DevelopmentConfig')
    app.config.from_envvar('APP_CONFIG', silent=True)

    load_assets(app)
    add_routes(app)
    return app

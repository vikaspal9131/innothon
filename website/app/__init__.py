from flask import Flask
import os 
from .config import Config

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    from . import routes, auth, prediction

    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(prediction.bp)

    return app

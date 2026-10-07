import os
from flask import Flask
from app.config import Config
from app.backend import AIinteractiondemo
from app.routes.ai_interaction_route import ai_interaction



def create_app(config_class: type = Config)->Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    os.makedirs(app.instance_path, exist_ok=True)
    
    aiservice = AIinteractiondemo.ai_service()
    app.register_blueprint(ai_interaction(aiservice), url_prefix="/")

    
    return app
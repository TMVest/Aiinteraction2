import os
from flask import Flask
from app.config import Config
from app.backend import AIinteractiondemo



def create_app(config_class: type = Config)->Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    os.makedirs(app.instance_path, exist_ok=True)

    aiservice = AIinteractiondemo


    
    return app
from flask import Flask
from .configuration import Config

app = Flask(__name__)  # Flask instance creation
app.config.from_object(Config)

from app.blueprints.home import home  # import main page

app.register_blueprint(home)

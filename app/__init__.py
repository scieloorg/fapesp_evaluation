from flask import Flask
from flask_script import Manager
from flask_mongoengine import MongoEngine
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

manager = Manager(app)

from app.models import models, forms
from app.controllers import default

app.wsgi_app = ProxyFix(app.wsgi_app)

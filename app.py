from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from os.path import abspath, dirname

import sys

sys.path.append(abspath(dirname(__file__)))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Import models here to migrate
from models.network import Network
from models.job import Job
from models.client import Client
from models.report import Report

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_socketio import SocketIO
from flask_cors import CORS
from flask import render_template, request,session
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config["SESSION_PERMANENT"] = False
# set the storage as Redis
app.config["SESSION_TYPE"] = "redis"

Session(app)

socketio = SocketIO(app,cors_allowed_origins='*',async_mode="gevent",manage_session=False )

from app import routes
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'
socketio = SocketIO(app)

from app import routes, socketio_events
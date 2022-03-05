import os

from app import socketio,app

if __name__ == '__main__':
    socketio.run(app,debug=os.getenv('DEBUG'), port=os.getenv('APP_PORT'))

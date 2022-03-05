
import datetime
from time import time
from xmlrpc.client import DateTime
from app import app
from app import db
from app import socketio
from flask_socketio import send,emit,join_room,leave_room
from flask import render_template, request,session



def index():

    response = render_template('index.html')
    return response


def chat_room():
    if request.method == "POST":
        params = dict(request.form)
        session['name'] = params.get('name')
        session['room_no'] = params.get('room_number')

    return render_template('chat.html')





# On general Chat message
@socketio.on('message')
def send_message(data):

    room = str(data.get('room_no'))
    message = data.get('message')
    timestamp = str(datetime.datetime.now())
    message = {
        'message':message,
        'timestamp': timestamp
    }

    # join room
    join_room(room)
    # send message in room
    emit('message',message,to=room,broadcast=True)

# On Chat message
@socketio.on('chat-message')
def chat_message(data):
    print('chat message received')
    room = data.get('room_no')    
    message = data.get('message')
    timestamp = str(datetime.datetime.now())
    message = {
        'message':message,
        'timestamp': timestamp,
        'name':session.get('name')
    }
    print(message)

    # send message in room
    emit('message',message,to=room,broadcast=True)


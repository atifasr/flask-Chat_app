from app import app
from app.communication.controllers import index,chat_room

app.add_url_rule('/','index',index,methods=['GET'])

app.add_url_rule('/chat','chat_room',chat_room,methods=['POST','GET'])
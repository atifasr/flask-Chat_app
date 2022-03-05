
from app import db
from sqlalchemy import func

class Chat(db.Model):
    date_created = db.Column()
    date_updated =  db.Column()
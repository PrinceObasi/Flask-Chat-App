# models.py
import flask_sqlalchemy
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    imageUrl = db.Column(db.String(256))

    def __init__(self, u, i):
        self.username = u
        self.imageUrl = i


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    imageUrl = db.Column(db.String(256))
    messageText = db.Column(db.String(256))
    timestamp = db.Column(db.String(128))

    def __init__(self, user, text, time, i):
        self.username = user
        self.messageText = text
        self.timestamp = time
        self.imageUrl = i


db.create_all()

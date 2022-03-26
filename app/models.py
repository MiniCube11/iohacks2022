from app import db, login
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    description = db.Column(db.String(2000), index=True)
    website_link = db.Column(db.String(200), index=True)
    register_link = db.Column(db.String(200), index=True)
    date = db.Column(db.DateTime, index=True)
    location = db.Column(db.String(300), index=True)
    is_virtual = db.Column(db.Boolean, index=True)

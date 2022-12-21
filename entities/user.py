import datetime
from flask_login import UserMixin
from extensions import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    visited = db.relationship('Places', backref='user')
    date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return f"<users {self.id}>"

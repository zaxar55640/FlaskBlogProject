from extensions import db
from datetime import datetime

class Places(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    visitors = db.Column(db.Integer, db.ForeignKey('user.id'))
    area = db.Column(db.String(20), nullable=False)
    img = db.Column(db.LargeBinary, nullable=True)
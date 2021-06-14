from app import db

class Mood(db.Model):
    """Mood model"""
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(80), nullable=False)
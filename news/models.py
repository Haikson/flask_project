from datetime import datetime
from app import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    intro = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    actual = db.Column(db.Integer, nullable=False)
    meta_description = db.Column(db.String(255), nullable=True)
    meta_keywords = db.Column(db.String(255), nullable=True)

    def __init__(self, title, intro=None, actual=30, description=None, meta_description=None, meta_keywords=None):
        self.date = datetime.now()
        self.title = title
        if intro is None:
            intro = description[:255]
        self.intro = intro
        self.actial = actual
        self.description = description
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
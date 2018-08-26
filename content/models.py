from datetime import datetime
from pytils.translit import slugify
from app import db


class Content(db.Model):
    __tablename__ = 'content'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), unique=True, nullable=False)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=True)
    publicate = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    last_modified = db.Column(db.DateTime)

    def __init__(self, title, content, publicate=False, slug=None):
        self.title = title
        self.content = content
        self.publicate = publicate
        self.last_modified = datetime.now()
        self.slug = slug if slug else slugify(title)

    def __repr__(self):
        return '<Content %r>'.format(self.title)


class PublicationCategory(db.Model):
    __tablename__ = 'publication_categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(60), unique=True, nullable=True)
    # publications = relationship("Publication", back_populates="category_id")

    def __init__(self, title, slug=None):
        self.title = title
        self.slug = slug if slug else slugify(title)

    def __repr__(self):
        return '<Content %r>'.format(self.title)


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    intro = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('publication_categories.id'), nullable=True)
    publicate = db.Column(db.Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow())
    last_modified = db.Column(db.DateTime)

    # category = relationship("PublicationCategory", back_populates="publications", foreign_keys="Publication.category_id")

    def __init__(self, title, content, category_id, intro=None, publicate=False, slug=None):
        self.title = title
        self.intro = intro
        self.content = content
        self.publicate = publicate
        self.category_id = category_id
        self.last_modified = datetime.now()
        self.slug = slug if slug else slugify(title)

    def __repr__(self):
        return '<Content %r>'.format(self.title)


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
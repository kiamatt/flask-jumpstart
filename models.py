from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    books = db.relationship('Book', backref='user', lazy='dynamic')

    @staticmethod
    def get_all():
        return User.query.all()

    def __repr__(self):
        return "<User: '{}', '{}'>".format(self.username, self.email)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Book: '{}'>".format(Book.url)
from exts import db
import datetime
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    tel = db.Column(db.String(11), nullable=False)
    password = db.Column(db.String(16), nullable=False)
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(100),nullable=False)
    title = db.Column(db.String(200),nullable=False)
    context = db.Column(db.Text,nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User',backref=db.backref('questions'))
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text,nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.now())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.relationship('Question', backref=db.backref('comment', order_by = id.desc()))
    author = db.relationship('User', backref=db.backref('comment'))
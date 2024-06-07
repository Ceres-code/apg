# app/models.py

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.schema import ForeignKeyConstraint
from datetime import datetime, timezone

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    reset_token = db.Column(db.String(100), nullable=True)
    profile_picture = db.Column(db.String(120), nullable=True)

    top_10 = db.relationship('UserTop10', backref='user', lazy=True)
    top_5 = db.relationship('UserTop5', backref='user', lazy=True)
    wish_list = db.relationship('UserWishList', backref='user', lazy=True)
    friends = db.relationship('Friendship', foreign_keys='Friendship.user_id', backref='initiator', lazy='dynamic')
    friend_requests = db.relationship('Friendship', foreign_keys='Friendship.friends_id', backref='recipient', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movies(db.Model):
    __bind_key__ = 'movies'
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    released_year = db.Column(db.String(4))
    title = db.Column(db.String(255))
    production_company = db.Column(db.String(255))
    cast = db.Column(db.Text)
    crew = db.Column(db.Text)
    runtime = db.Column(db.Integer)
    genre = db.Column(db.String(255))

class Cast(db.Model):
    __bind_key__ = 'movies'
    __tablename__ = 'cast'
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), primary_key=True)
    image_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Directors(db.Model):
    __bind_key__ = 'movies'
    __tablename__ = 'directors'
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), primary_key=True)
    image_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class UserRating(db.Model):
    __bind_key__ = 'movies'
    __tablename__ = 'user_rating'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    rating = db.Column(db.Integer)

    user = db.relationship('User', backref='ratings', lazy='dynamic')
    movie = db.relationship('Movies', backref='ratings', lazy='dynamic')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'movie_id', name='_user_movie_uc'),
    )

class UserTop5(db.Model):
    __tablename__ = 'user_top_5_dir'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    director_image_id = db.Column(db.Integer, primary_key=True)

class UserTop10(db.Model):
    __tablename__ = 'user_top_10'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    movie_id = db.Column(db.Integer, primary_key=True)

class UserWishList(db.Model):
    __tablename__ = 'user_wish_list'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    movie_id = db.Column(db.Integer, primary_key=True)

class Friendship(db.Model):
    __tablename__ = 'friends_list'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    friends_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_friends_list_user_id'),
        ForeignKeyConstraint(['friends_id'], ['user.id'], name='fk_friends_list_friends_id'),
        ForeignKeyConstraint(['status_id'], ['status.id'], name='fk_friends_list_status_id'),
    )

class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)

class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    replies = db.relationship('Reply', backref='topics', lazy=True)

class Reply(db.Model):
    __tablename__ = 'replies'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movies = db.relationship('ListItem', back_populates='list')

class ListItem(db.Model):
    __tablename__ = 'list_item'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    list = db.relationship('List', back_populates='movies')
    movie = db.relationship('Movies', backref='list_items')

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    read = db.Column(db.Boolean, default=False, nullable=False)

    sender = db.relationship('User', foreign_keys=[sender_id], backref=db.backref('sent_messages', lazy='dynamic'))
    recipient = db.relationship('User', foreign_keys=[recipient_id], backref=db.backref('received_messages', lazy='dynamic'))

class FriendRequest(db.Model):
    __tablename__ = 'friend_request'
    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    requestee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(10), default='pending')
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    requester = db.relationship('User', foreign_keys=[requester_id], backref='sent_requests')
    requestee = db.relationship('User', foreign_keys=[requestee_id], backref='received_requests')

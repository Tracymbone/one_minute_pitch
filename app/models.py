from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


class User(UserMixin,db.Model):
    __tablename__="users"
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),index=True)
    email=db.Column(db.String(255),index=True)
    biography=db.Column(db.String(255))
    profile_pic=db.Column(db.String())
    password_secure=db.Column(db.String(255))
    posts= db.relationship('Post',backref = 'user',lazy ="dynamic")
    like = db.relationship('Like',backref='user',lazy='dynamic')
    dislike = db.relationship('Dislike',backref='user',lazy='dynamic')
    comment = db.relationship('Comment',backref='user',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)

    def __repr__(self):
        return f'User: {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def __repr__(self):
    return f'User: {self.name}'



class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    post = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    like = db.relationship('Like',backref='new',lazy='dynamic')
    dislike = db.relationship('Dislike',backref='new',lazy='dynamic')
    comment = db.relationship('Comment',backref='new',lazy='dynamic')


    def save_post(self):
        db.session.add(self)
        db.session.commit()


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        like_response = Like.query.filter_by(post_id=id).all()
        return like_response

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Dislike(db.Model):
    __tablename__ = 'dislikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_dislikes(cls, id):
        dislike_response =Dislike.query.filter_by(post_id=id).all()
        return dislike_response

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comments_results = Comment.query.filter_by(post_id=post_id).all()

        return comments_results

    def __repr__(self):
        return f'comment:{self.comment}'




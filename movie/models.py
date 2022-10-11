from movie import db, ma
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import date

class Users(db.Model):
  __tablename__ = "users"

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  first_name = db.Column(db.String(), nullable=False)
  last_name = db.Column(db.String(), nullable=False)
  user_name = db.Column(db.String(), nullable=False)
  password = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False, unique=True)
  reviews = db.relationship('Reviews', backref='author', lazy=True)
  to_watch = db.relationship('Watch', backref='watch', lazy=True)

  def __init__(self, first_name, last_name, user_name, password, email):
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.password = password
    self.email = email

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'first_name', 'last_name', 'user_name', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Reviews(db.Model):
  __tablename__ = 'reviews'

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  movie_id = db.Column(db.String(), nullable=False)
  title = db.Column(db.String(), nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  review = db.Column(db.String(500), nullable=True)
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)

  def __init__(self, movie_id, title, rating, review, user_id):
    self.movie_id = movie_id
    self.title = title
    self.rating = rating
    self.review = review
    self.user_id = user_id

class ReviewSchema(ma.Schema):
  class Meta:
    fields = ('title', 'rating', 'review')

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

class Friends(db.Model):
  __tablename__ = "friends"

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  user_one_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
  user_two_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
  friend_one = db.relationship("Users", foreign_keys=[user_one_id], backref=db.backref("friend_one"))
  friend_two = db.relationship("Users", foreign_keys=[user_two_id], backref=db.backref("friend_two"))
  date_created = db.Column(db.String() , nullable=False)

  def __init__(self, user_one_id, user_two_id, date_created=date.today()):
    self.user_one_id = user_one_id
    self.user_two_id = user_two_id
    self.date_created = date_created

class FriendsSchema(ma.Schema):
  class Meta:
    fields = ('user_one_id', 'user_two_id')

friend_schema = FriendsSchema()

class Watch(db.Model):
  __tablename__ = "to_watch"

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
  movie_id = db.Column(db.String(), nullable=False)
  title = db.Column(db.String(), nullable=False)
  date_created = db.Column(db.String(), nullable=False)
  
  def __init__(self, user_id, movie_id, title, date_created=date.today()):
    self.user_id = user_id
    self.movie_id = movie_id,
    self.title = title,
    self.date_created = date_created

class WatchSchema(ma.Schema):
  class Meta:
    fields = ('user_id', 'movie_id', 'title')

watch_schema = WatchSchema()

class Suggestions(db.Model):
  __tablename__ = "suggestions"

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  user_one_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
  user_two_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
  user_one = db.relationship("Users", foreign_keys=[user_one_id], backref=db.backref("user_one"))
  user_two = db.relationship("Users", foreign_keys=[user_two_id], backref=db.backref("user_two"))
  movie_id = db.Column(db.String(), nullable=False)
  title = db.Column(db.String(), nullable=False)

  def __init__(self, user_one_id, user_two_id, movie_id, title):
    self.user_one_id = user_one_id
    self.user_two_id = user_two_id
    self.movie_id = movie_id
    self.title = title

  class SuggestionSchema(ma.Schema):
    class Meta:
      fields = ('user_one', 'user_two', 'movie_id', 'title')

  suggestion_schema = SuggestionSchema()
  suggestions_shema = SuggestionSchema(many=True)

"""
TODO
1) add way to make friends (finish connecting friends to users)
2) add way to suggest movies/shows
3) add all of the logic surrounding that
"""

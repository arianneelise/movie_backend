from movie import db, ma
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Users(db.Model):
  __tablename__ = "users"

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  first_name = db.Column(db.String(), nullable=False)
  last_name = db.Column(db.String(), nullable=False)
  user_name = db.Column(db.String(), nullable=False)
  password = db.Column(db.String(), nullable=False)
  email = db.Column(db.String(), nullable=False, unique=True)
  reviews = db.relationship('Reviews', backref='author', lazy=True)

  def __init__(self, first_name, last_name, user_name, password, email):
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.password = password
    self.email = email

class UserSchema(ma.Schema):
  class Meta:
    fields = ('first_name', 'last_name', 'user_name', 'email')

user_schema = UserSchema()

class Reviews(db.Model):
  __tablename__ = 'reviews'

  id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, nullable=False, unique=True)
  title = db.Column(db.String(), nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  review = db.Column(db.String(500), nullable=True)
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)

  def __init__(self, title, rating, review, user_id):
    self.title = title
    self.rating = rating
    self.review = review
    self.user_id = user_id

class ReviewSchema(ma.Schema):
  class Meta:
    fields = ('title', 'rating', 'review')

review_schema = ReviewSchema()

"""
TODO
1) connect to api
2) create endpoint 'add review'
3) create endpoint 'get review by id'
"""

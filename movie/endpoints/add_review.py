import flask 
from flask import jsonify
from movie import db
from movie.models import Reviews, review_schema

def add_review(req:flask.Request) -> flask.Response:
  response = req.get_json()
  id = response.get('id')
  title = response.get('title')
  rating = response.get('rating')
  review = response.get('review')
  user_id = response.get('user_id')

  review = Reviews(id, title, rating, review, user_id)
  db.session.add(review)
  db.session.commit()

  return jsonify(review_schema.dump(review))
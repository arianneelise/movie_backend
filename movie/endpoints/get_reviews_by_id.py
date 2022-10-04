import flask
from flask import jsonify
from movie.models import Reviews, review_schema, user_schema
from movie import db

def get_reviews_by_id(req:flask.Request) -> flask.Response:
  response = req.get_json()
  movie_id = response.get("movie_id")
  response_object = []

  reviews = db.session.query(Reviews).filter(Reviews.movie_id == movie_id).all()

  for review in reviews: 
    new_dict = {"review": review_schema.dump(review), "author": user_schema.dump(review.author)}
    response_object.append(new_dict)

  return jsonify(response_object)
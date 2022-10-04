import flask
from flask import jsonify
from movie import db
from movie.models import Reviews, Users, reviews_schema

def get_review(req:flask.Request) -> flask.Response:
  response = req.get_json()
  user_id = response.get("user_id")

  user = db.session.query(Users).filter(Users.id == user_id).first()
  
  return jsonify(reviews_schema.dump(user.reviews))
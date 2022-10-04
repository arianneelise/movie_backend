import flask
from flask import jsonify
from movie import db
from movie.models import Users, users_schema

def get_all_users(req:flask.Request) -> flask.Response:
  all_users = db.session.query(Users).all()
  return jsonify(users_schema.dump(all_users))

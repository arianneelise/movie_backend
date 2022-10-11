import flask 
from flask import jsonify
from movie.models import Users, user_schema, Friends, friend_schema
from movie import db

def add_friend(req:flask.Request) -> flask.Response:
  response = req.get_json()
  user_one_id = response.get("user_one_id")
  user_two_id = response.get("user_two_id")

  new_friends = Friends(user_one_id, user_two_id)
  db.session.add(new_friends)
  db.session.commit()

  print(new_friends)

  return "hello"
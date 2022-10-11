import flask 
from flask import jsonify
from movie.models import Users, user_schema, Friends, friend_schema
from movie.util import verify_user
from movie import db

def add_friend(req:flask.Request) -> flask.Response:
  response = req.get_json()
  user_one_id = response.get("user_one_id")
  user_two_id = response.get("user_two_id")
  friend_check = db.session.query(Friends).filter(Friends.user_one_id == user_one_id).all()

  print(friend_check)

  for item in friend_check:
    if str(item.user_one_id) == user_two_id or str(item.user_two_id) == user_two_id:
      return jsonify("Record already exists"), 400

  new_friends = Friends(user_one_id, user_two_id)
  db.session.add(new_friends)
  db.session.commit()

  if verify_user.verify_user(user_one_id) and verify_user.verify_user(user_two_id):
    return jsonify(friend_schema.dump(new_friends)), 200

  

    

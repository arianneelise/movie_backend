import flask 
from flask import jsonify
from movie.models import Friends, friend_schema
from movie import util
from movie import db
from sqlalchemy import or_

def add_friend(req:flask.Request) -> flask.Response:
  response = req.get_json()
  user_one_id = response.get("user_one_id")
  user_two_id = response.get("user_two_id")

  if util.verify_user(user_one_id) and util.verify_user(user_two_id):
    friend_check = db.session.query(Friends).filter(or_(Friends.user_one_id == user_one_id, Friends.user_two_id == user_one_id)).all()

    for item in friend_check:
      if str(item.user_one_id) == user_two_id or str(item.user_two_id) == user_two_id:
        return jsonify("Record already exists"), 400

    new_friends = Friends(user_one_id, user_two_id)
    db.session.add(new_friends)
    db.session.commit()

    return jsonify(friend_schema.dump(new_friends)), 200

  else:
    return jsonify("One or more invalid ids"), 400

  

    

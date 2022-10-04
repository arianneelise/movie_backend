import flask 
from flask import jsonify
from movie.models import Users, user_schema
from movie import db

def add_user(req:flask.Request, bcrypt) -> flask.Response:
  response = req.get_json()
  first_name = response.get("first_name")
  last_name = response.get("last_name")
  user_name = response.get("user_name")
  password = response.get("password")
  password_bytes = password.encode("utf-8")
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password_bytes, salt)
  email = response.get("email")

  new_user = Users(first_name,last_name,user_name,hashed_password,email)
  db.session.add(new_user)
  db.session.commit()

  return jsonify(user_schema.dump(new_user))
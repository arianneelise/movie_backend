import flask 
from flask import jsonify
from movie.models import Users, user_schema
from movie import db

def verify_user(id):
  user_check = db.session.query(Users).filter(Users.id == id).first()
  if user_check:
    return True
  else:
    return False

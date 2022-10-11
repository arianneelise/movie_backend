from uuid import UUID
import flask 
from flask import jsonify
from movie.models import Users, user_schema
from movie import db

def verify_user(id):
  try:
    verify_id = UUID(id, version=4)
    user_check = db.session.query(Users).filter(Users.id == verify_id).first()
    if user_check:
      return True
    else:
      return False
  except:
    return False

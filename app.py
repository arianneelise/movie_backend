from crypt import methods
from movie import app
from flask import request
from movie import endpoints
import bcrypt
# from movie.endpoints import add_user, search_movie, add_review, get_all_users, get_review, get_reviews_by_id

@app.route('/add-user', methods=["POST"])
def add():
  return endpoints.add_user(request, bcrypt)

@app.route('/search', methods=["POST"])
def search():
  return endpoints.search_movie(request)

@app.route('/add-review', methods=["POST"])
def review():
  return endpoints.add_review(request)

@app.route('/get-all-users', methods=["GET"])
def get_users():
  return endpoints.get_all_users(request)

@app.route('/user/get-review', methods=["POST"])
def get_user_review():
  return endpoints.get_review(request)

@app.route('/get-reviews', methods=["POST"])
def get_reviews():
  return endpoints.get_reviews_by_id(request)

if __name__ == '__main__':
  app.run()
from movie import app
from flask import request
from movie.endpoints import add_user, search_movie, add_review, get_all_users, get_review
import bcrypt

@app.route('/add-user', methods=["POST"])
def add():
  return add_user.add_user(request,bcrypt)

@app.route('/search', methods=["POST"])
def search():
  return search_movie.search_movie(request)

@app.route('/add-review', methods=["POST"])
def review():
  return add_review.add_review(request)

@app.route('/get-all-users', methods=["GET"])
def get_users():
  return get_all_users.get_all_users(request)

@app.route('/user/get-review', methods=["POST"])
def get_user_review():
  return get_review.get_review(request)

if __name__ == '__main__':
  app.run()
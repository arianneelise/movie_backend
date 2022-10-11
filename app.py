from flask import request
from movie import app, endpoints
import bcrypt

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

@app.route('/add-friend', methods=["POST"])
def add_friend():
  return endpoints.add_friend(request)

if __name__ == '__main__':
  app.run()
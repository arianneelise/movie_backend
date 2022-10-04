from movie import app
from flask import request
from movie.endpoints import add_user, search_movie
import bcrypt

@app.route('/add-user', methods=["POST"])
def add():
  return add_user.add_user(request,bcrypt)

@app.route('/search', methods=["POST"])
def search():
  return search_movie.search_movie(request)

if __name__ == '__main__':
  app.run()
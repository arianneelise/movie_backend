from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Hey flask, this is where our app is running. This is where we are instantiating it.
app = Flask(__name__)
# Initialize database
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://standarduser:1234@localhost/movies'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
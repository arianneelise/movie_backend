import json
from movie import db
from movie.models import Users

def json_data():
  with open('MOCK_DATA.json', 'r') as myfile:
    data = myfile.read()

  obj = json.loads(data)

  for person in obj:
    user = Users(person["first_name"], person["last_name"], person["user_name"], person["password"], person["email"])
    db.session.add(user)
    db.session.commit()
  
  return obj

json_data()
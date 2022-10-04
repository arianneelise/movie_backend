import json
from operator import pos
import flask 
from movie.utelly_request import utelly_request

def search_movie(req:flask.Request) -> flask.Response:
  response = req.get_json()
  search_term = response.get("term")
  request_body = {"term": search_term}

  result = utelly_request("lookup", request_body)
  final_results = []

  for r in result["results"]:
    r_dictionary = {
      'id' : r['id'],
      'name': r["name"],
      'picture': r["picture"],
      'watch': []
    }

    for l in r["locations"]:
      r_dictionary['watch'].append({"service": l["display_name"], "url": l["url"]})
  
    final_results.append(r_dictionary)
  
  return final_results
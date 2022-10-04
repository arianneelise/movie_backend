import requests  

"""Body can be {"source_id":"tt3398228","source":"imdb","country":"us"} or {"term":"bojack","country":"uk"} !!Country is optional in both circumstances
type can be "idlookup" (which goes with the former body) or "lookup" (which goes with the latter)"""

def utelly_request(type, body):
  url = f"https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/{type}"
  headers = {
  "X-RapidAPI-Key": "7449c2b2c4mshf048a4769e6c71bp140a41jsn5cbc83512c8a",
  "X-RapidAPI-Host": "utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com"
  } 

  response = requests.request("GET", url, headers=headers, params=body)

  return response.json()
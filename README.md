Run `gunicorn serve:app` on the root directory of the project to run server on port 8000

Url Mapprings:

1. http://localhost:8000
  - Redirects to http://localhost:8000/status which should responde with `{"status":"server is running"}`
  
 
2. http://localhost:8000/nba/player/{last_name}
  - Responds with and empty list `[]` if there are no players by that last name or with a list of json objects of type `{id = String, name = String}`
  

3. http://localhost:8000/nba/player/{player_id}/stats
  - Responds with a json object of type `{Rebounds = [], Assists = [], Points = []}` which are the player's latest rebounds, assists and points

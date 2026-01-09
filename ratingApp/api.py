import requests
from django.conf import settings

def search_movies_api(query,params):
    url = "https://api.themoviedb.org/3/search/movie"
    

    response = requests.get(url, params=params)
    #response.raise_for_status()
    return response.json()

def search_moviesByID(movie_id):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = { 
        "api_key": settings.API_KEY,
        "language": "en-US" }
    response = requests.get(url,params=params)
    data = response.json() 
    
    return data
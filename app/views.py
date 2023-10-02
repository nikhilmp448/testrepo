from django.shortcuts import render
import imdb
import requests
from bs4 import BeautifulSoup


api_key = "fada996915db97d2c433bc87692e1fca"

def get_popular():
    url = "https://api.themoviedb.org/3/person/popular"

    params = {
        "api_key": 'api_key',
        "page": 1,  
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.status_code
    
def get_trending_movies():
    url = "https://api.themoviedb.org/3/trending/movie/day"
    

    params = {
        "api_key": api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        trending_movies = response.json()
        return trending_movies.get("results", [])
    else:
        return []
    
def get_trending_movie_posters():
    trending_movies = get_trending_movies()

    poster_urls = []
    for movie in trending_movies:
        poster_path = movie.get("poster_path")
        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w200/{poster_path}"
            poster_urls.append(poster_url)

    return poster_urls

def now_showing_movies():
    url = "https://api.themoviedb.org/3/movie/now_playing"

    params = {
        "api_key": api_key,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        now_showing_movies = response.json()
        return now_showing_movies.get("results", [])
    else:
        return []



def home(request):
    popular = get_popular()
    # trending = get_trending_movies()
    now_streaming = now_showing_movies()

    trending_movie_poster = get_trending_movie_posters()


    context = {'popular':popular,
               'trending':trending_movie_poster
               }
    return render(request,'index.html',context)
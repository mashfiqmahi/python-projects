from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Movie
from .forms import RateMovieForm, AddMovieForm
import requests

# Constants ( Ideally, put these in settings.py, but keeping here for simplicity as requested)
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
API_KEY = "cb7115b0e7a169e60baf214f2d0126b4"  # Your provided Key


def home(request):
    # Get all movies, order by rating (descending)
    all_movies = Movie.objects.all().order_by('-rating')

    # Re-calculate ranking based on position
    # Note: In Django we usually don't save computed fields back to DB on every read
    # for performance, but I will replicate your Flask logic exactly.
    for i, movie in enumerate(all_movies):
        movie.ranking = i + 1
        movie.save()

    return render(request, "movies/index.html", {"movies": all_movies})


def add_movie(request):
    form = AddMovieForm()
    if request.method == "POST":
        form = AddMovieForm(request.POST)
        if form.is_valid():
            movie_title = form.cleaned_data['title']
            response = requests.get(
                MOVIE_DB_SEARCH_URL,
                params={"api_key": API_KEY, "query": movie_title}
            )
            data = response.json().get('results', [])
            return render(request, "movies/select.html", {"options": data})

    return render(request, "movies/add.html", {"form": form})


def find_movie(request, tmdb_id):
    response = requests.get(
        f"{MOVIE_DB_INFO_URL}/{tmdb_id}",
        params={"api_key": API_KEY, "language": "en-US"}
    )
    data = response.json()

    new_movie = Movie.objects.create(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
    )
    return redirect('edit_movie', movie_id=new_movie.id)


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = RateMovieForm(instance=movie)

    if request.method == "POST":
        form = RateMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "movies/edit.html", {"form": form, "movie": movie})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('home')
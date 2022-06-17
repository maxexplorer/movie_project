from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Max, Min, Count, Avg
from .models import Movie, Director, Actor, Feedback
from .forms import FeedbackForm

# Create your views here.


def show_all_movies(request):
    movies = Movie.objects.order_by('-rating')
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    form = FeedbackForm()
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
        'form': form
    })

def show_all_directors(request):
    directors = Director.objects.order_by('last_name')
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors
    })


def show_director(request, slug_director: str):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/info_director.html', {
        'director': director
    })


def show_all_actors(request):
    actors = Actor.objects.order_by('last_name')
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors
    })


def show_actor(request, slug_actor: str):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/info_actor.html', {
        'actor': actor
    })


def done(request):
    FeedbackForm(request.POST).save()
    return render(request, 'movie_app/done.html')

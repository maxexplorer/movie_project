from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('done', views.done),
    path('directors', views.show_all_directors),
    path('actors', views.show_all_actors),
    path('directors/<slug:slug_director>', views.show_director, name='info_director'),
    path('actors/<slug:slug_actor>', views.show_actor, name='info_actor'),
]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('director', views.show_all_directors),
    path('director/<slug:slug_director>', views.show_director, name='info_director'),
]

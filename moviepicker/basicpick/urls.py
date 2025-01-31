from django.urls import path

from . import views

app_name = "basicpick"

urlpatterns = [
    path("", views.index, name="index"),
    path("result", views.FilterView, name="result"),
    path("result/error", views.ErrorView, name="error"),
    path("result/<int:movie_pk>/watched", views.WatchedView, name="watched"),
    path("updatemovie/<int:movie_pk>", views.UpdateWatchedMovie, name="updatewatchedmovie"),
]
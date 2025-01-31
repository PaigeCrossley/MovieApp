from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

from .models import Movie 
from .forms import BPModelForm, WatchedModelForm

# Create your views here.
def index(request):
    context = {
        'form': BPModelForm(),
    }
    return render(request, "basicpick/index.html", context)

def FilterView(request):
    qs = Movie.objects.all()

    possible_genres = request.GET.getlist("movie_genre")
    possible_rewatch = request.GET.get("rewatch")

    if possible_rewatch == 2:
        try:
            qs = qs.filter(movie_genre__in = possible_genres)
            item_count = qs.count()
            random_item = qs[random.randint(0,item_count-1)]
        except:
            return redirect('basicpick:error')
    else:
        try:
            qs = qs.filter(movie_genre__in = possible_genres, rewatch = possible_rewatch)
            item_count = qs.count()
            random_item = qs[random.randint(0,item_count-1)]
        except:
            return redirect('basicpick:error')

    context = {
        'queryset': random_item,
    }

    return render(request, "basicpick/filterview.html", context)

def ErrorView(request):
    return render(request, "basicpick/errorview.html")

def WatchedView(request, movie_pk):

    context = {
        'form': WatchedModelForm(),
        'movie_pk': movie_pk,
    }
    
    return render(request, "basicpick/watchedview.html", context)

def UpdateWatchedMovie(request, movie_pk):
    watched_movie = Movie.objects.get(pk=movie_pk)
    watched_movie.watched = True
    watched_movie.rewatch = request.POST['rewatch']
    watched_movie.date_watched=datetime.today()
    watched_movie.save()
    return HttpResponseRedirect(reverse('basicpick:index'))

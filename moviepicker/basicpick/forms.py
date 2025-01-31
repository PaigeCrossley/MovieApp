from django import forms

from .models import Movie

class BPModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["movie_genre", "rewatch"]
        widgets = {
            "movie_genre": forms.CheckboxSelectMultiple(attrs={'rows': 10, 'cols': 20, 'title': "Movie Genres:",}),
            "rewatch": forms.Select(choices=[(False, "Only movies we've never seen before"), (True, "Only movies we've seen before"), (2, "Either!")], attrs={'title': "Watch Status:",})
        }

class WatchedModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["rewatch"]
        widgets = {
            "rewatch": forms.Select(choices=[(True, "Yes, please!"), (False, "No thanks")])
        }
                
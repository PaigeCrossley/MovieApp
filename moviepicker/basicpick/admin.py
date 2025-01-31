from django.contrib import admin

from .models import Movie, Genre, MovieGenre

# Register your models here.
class MovieGenreInLine(admin.TabularInline):
    model = MovieGenre
    max_num = 2

class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieGenreInLine]
    list_display = ["movie_name", "release_year"]
    search_fields = ["movie_name"]
    list_filter = ["watched", "rewatch", "movie_genre"]
   
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(MovieGenre)

# Change Admin "View Site" URL to point to basicpick
admin.site.site_url = "/basicpick"
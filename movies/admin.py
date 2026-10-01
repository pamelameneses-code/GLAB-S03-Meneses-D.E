from django.contrib import admin
from .models import Genre, Person, Movie, Rating

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ('created_at',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'created_at', 'updated_at')
    list_filter = ('release_year', 'genres')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('genres', 'directors')
    inlines = [RatingInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'score', 'created_at')
    list_filter = ('score',)
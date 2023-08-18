from django import forms
from django.contrib import admin

from musicpedia.music.models import Label, Genre, Instrument, Album, Song, Artist


class LabelAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']


class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['name']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']


class SongAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
from django import forms
from django.contrib import admin

from musicpedia.accounts.models import Profile
from musicpedia.music.models import Label, Genre, Instrument, Album, Song, Artist, MusicianInstruments, Review


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']


class MusicianInstrumentsAdmin(admin.ModelAdmin):
    list_display = ['musician']


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(MusicianInstruments, MusicianInstrumentsAdmin)
admin.site.register(Review, ReviewAdmin)
import datetime

from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=50)
    image = models.ImageField(upload_to='labels', blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=50, default='')
    years_active = models.CharField(max_length=12, default='')
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artists')
    description = models.TextField(default='')
    status = models.BooleanField(default=True)
    born = models.DateField(blank=True, null=True)
    solo = models.BooleanField(default=True)
    is_band = models.BooleanField(default=True)

    def first_letter(self):
        return self.name[0].upper()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ArtistGenres(models.Model):
    artist = models.ForeignKey(Artist, default='', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class BandMembers(models.Model):
    band = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='band')
    member = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='member')
    present_member = models.BooleanField(default=True)
    years_active = models.CharField(max_length=12, default='')


class Instrument(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MusicianInstruments(models.Model):
    musician = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musician_instrument')
    band = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='musician_instrument_band')
    instrument = models.ForeignKey(Instrument, default='', on_delete=models.CASCADE)


class Album(models.Model):
    title = models.CharField(max_length=255)
    released = models.DateField(default=datetime.date.today)
    artist = models.ForeignKey(Artist, default=1, blank=True, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    album_cover = models.ImageField(default='', upload_to='album_covers')
    length = models.DurationField(default='')

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, blank=True, on_delete=models.CASCADE)
    released = models.DateField(default=datetime.date.today)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    song_cover = models.ImageField(default='', blank=True, null=True, upload_to='song_covers')
    length = models.DurationField(default='')

    def __str__(self):
        return self.title
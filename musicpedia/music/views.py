from itertools import chain

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from musicpedia.accounts.models import Profile
from musicpedia.music.forms import LabelForm, ArtistForm, GenreForm, InstrumentForm, BandMembersForm, \
    MusicianInstrumentsForm, ArtistGenresForm, EditArtistForm, AlbumForm, EditAlbumForm, SongForm
from musicpedia.music.models import Artist, BandMembers, ArtistGenres, Album, Song


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home.html', context=context)


@login_required
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArtistForm()
    context = {
        'form': form,
    }

    return render(request, 'artists/new-artist.html', context)


@login_required
def add_label(request):
    if request.method == 'POST':
        form = LabelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LabelForm()
    context = {
        'form': form,
    }

    return render(request, 'labels/new-label.html', context)


@login_required
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GenreForm()
    context = {
        'form': form,
    }

    return render(request, 'genres/new-genre.html', context)


@login_required
def add_instrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InstrumentForm()
    context = {
        'form': form,
    }

    return render(request, 'instruments/new-instrument.html', context)


def artists(request):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    context = {
        'alphabet': alphabet
    }
    return render(request, 'artists.html', context)


def by_letter(request, letter):
    solo_artists = Artist.objects.filter(solo=True)
    bands = Artist.objects.filter(is_band=True)
    artists = list(chain(solo_artists, bands))
    artists = [artist for artist in artists if artist.first_letter() == letter]
    context = {
        'artists': artists
    }
    return render(request, 'by_letter.html', context)


def artist_details(request, pk):
    artist = Artist.objects.get(pk=pk)

    context = {
        'artist': artist
    }
    return render(request, 'artists/artist_details.html', context)


@login_required
def edit_artist_info(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=artist.id)
    else:
        form = EditArtistForm(instance=artist)
    context = {
        'form': form,
        'artist': artist,
    }
    return render(request, 'artists/edit_artist_info.html', context)


@login_required
def edit_band_members(request, pk):
    band = Artist.objects.get(pk=pk)

    band_members = BandMembers.objects.filter(band=pk)

    context = {
        'band': band,
        'band_members': band_members,
    }
    return render(request, 'artists/edit_band_members.html', context)


@login_required
def add_band_member(request, pk):
    band = Artist.objects.get(pk=pk)
    musicians = Artist.objects.filter(is_band=False)

    if request.method == 'POST':
        form = BandMembersForm(request.POST, request.FILES, initial={'band': band, 'member': musicians})
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=band.id)
    else:
        form = BandMembersForm(initial={'band': band})
    context = {
        'form': form,
        'band': band
    }

    return render(request, 'artists/add_band_member.html', context)


@login_required
def add_musician_instrument(request, pk):
    musician = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        form = MusicianInstrumentsForm(request.POST, request.FILES, initial={'musician': musician})
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=musician.id)
    else:
        form = MusicianInstrumentsForm(initial={'musician': musician})
    context = {
        'form': form,
        'musician': musician
    }

    return render(request, 'instruments/add_musician_instrument.html', context)


@login_required
def edit_artist_genres(request, pk):
    artist = Artist.objects.get(pk=pk)

    artist_genres = ArtistGenres.objects.filter(artist=pk)

    context = {
        'artist': artist,
        'artist_genres': artist_genres,
    }
    return render(request, 'genres/edit_artist_genres.html', context)


@login_required
def add_artist_genres(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArtistGenresForm(request.POST, request.FILES, initial={'artist': artist})
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=artist.id)
    else:
        form = ArtistGenresForm(initial={'artist': artist})
    context = {
        'form': form,
        'artist': artist
    }

    return render(request, 'genres/add_artist_genres.html', context)


@login_required
def add_album(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, initial={'artist': artist})
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=artist.id)
    else:
        form = AlbumForm(initial={'artist': artist})
    context = {
        'form': form,
        'artist': artist
    }

    return render(request, 'albums/new-album.html', context)


@login_required
def edit_artist_albums(request, pk):
    artist = Artist.objects.get(pk=pk)

    artist_albums = Album.objects.filter(artist=pk)

    context = {
        'artist': artist,
        'artist_albums': artist_albums,
    }
    return render(request, 'albums/edit-artist-albums.html', context)


@login_required
def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


@login_required
def edit_album_info(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album details', pk=album.id)
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'albums/edit-album-info.html', context)


@login_required
def edit_album_songs(request, pk):
    album = Album.objects.get(pk=pk)

    album_songs = Song.objects.filter(album=pk)

    if not album_songs:
        album_songs = []

    context = {
        'album': album,
        'album_songs': album_songs
    }
    return render(request, 'songs/edit_album_songs.html', context)


@login_required
def add_album_song(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES, initial={'album': album})
        if form.is_valid():
            form.save()
            return redirect('album details', pk=album.id)
    else:
        form = SongForm(initial={'album': album})
    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'songs/add_album_song.html', context)
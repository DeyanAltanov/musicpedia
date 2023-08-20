from itertools import chain

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, FormView
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect


from musicpedia.accounts.models import Profile
from musicpedia.music.forms import LabelForm, ArtistForm, GenreForm, InstrumentForm, BandMembersForm, \
    MusicianInstrumentsForm, ArtistGenresForm, EditArtistForm, AlbumForm, EditAlbumForm, SongForm, EditSongForm, \
    ReviewForm, EditReviewForm
from musicpedia.music.models import Artist, BandMembers, ArtistGenres, Album, Song, MusicianInstruments, Review, Genre, \
    Instrument, Label


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home.html', context=context)


# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def add_artist(request):
#     if request.method == 'POST':
#         form = ArtistForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ArtistForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'artists/new-artist.html', context)


class CreateArtistView(LoginRequiredMixin, CreateView):
    template_name = 'artists/new-artist.html'
    model = Artist
    fields = '__all__'
    success_url = reverse_lazy('home')
    request.user = staff_member_required


# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def add_label(request):
#     if request.method == 'POST':
#         form = LabelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = LabelForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'labels/new-label.html', context)


class CreateLabelView(LoginRequiredMixin, CreateView):
    template_name = 'labels/new-label.html'
    model = Label
    fields = '__all__'
    success_url = reverse_lazy('home')
    request.user = staff_member_required


# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def add_genre(request):
#     if request.method == 'POST':
#         form = GenreForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = GenreForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'genres/new-genre.html', context)


class CreateGenreView(LoginRequiredMixin, CreateView):
    template_name = 'genres/new-genre.html'
    model = Genre
    fields = '__all__'
    success_url = reverse_lazy('home')
    request.user = staff_member_required



# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def add_instrument(request):
#     if request.method == 'POST':
#         form = InstrumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = InstrumentForm()
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'instruments/new-instrument.html', context)



class CreateInstrumentView(LoginRequiredMixin, CreateView):
    template_name = 'instruments/new-instrument.html'
    model = Instrument
    fields = '__all__'
    success_url = reverse_lazy('home')
    request.user = staff_member_required


def artists(request):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    context = {
        'alphabet': alphabet
    }
    return render(request, 'artists.html', context)


def by_letter(request, letter):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    ]
    solo_artists = Artist.objects.filter(solo=True)
    bands = Artist.objects.filter(is_band=True)
    artists = list(chain(solo_artists, bands))
    artists = [artist for artist in artists if artist.first_letter() == letter]
    context = {
        'artists': artists,
        'alphabet': alphabet
    }
    return render(request, 'by_letter.html', context)


def artist_details(request, pk):
    artist = Artist.objects.get(pk=pk)
    albums = Album.objects.filter(artist=pk)
    bands = MusicianInstruments.objects.filter(musician=pk)
    present_band_members = BandMembers.objects.filter(band=pk, present_member=True)
    past_band_members = BandMembers.objects.filter(band=pk, present_member=False)
    genres = ArtistGenres.objects.filter(artist=pk)
    is_band = False
    for band in bands:
        if band.band:
            is_band = True
            break

    context = {
        'artist': artist,
        'albums': albums,
        'bands': bands,
        'present_band_members': present_band_members,
        'past_band_members': past_band_members,
        'genres': genres,
        'is_band': is_band
    }
    return render(request, 'artists/artist_details.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
def edit_band_members(request, pk):
    band = Artist.objects.get(pk=pk)

    band_members = BandMembers.objects.filter(band=pk)

    context = {
        'band': band,
        'band_members': band_members,
    }
    return render(request, 'artists/edit_band_members.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_band_member(request, pk):
    band = Artist.objects.get(pk=pk)
    band_members = BandMembers.objects.filter(band=band)

    if request.method == 'POST':
        form = BandMembersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=band.id)
    else:
        form = BandMembersForm(initial={'band': band})
        for member in band_members:
            form.fields['member'].queryset = Artist.objects.exclude(member=member).filter(is_band=False)

    context = {
        'form': form,
        'band': band,
    }

    return render(request, 'artists/add_band_member.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
def edit_musician_instruments(request, pk):
    musician = Artist.objects.get(pk=pk)

    musician_instruments = MusicianInstruments.objects.filter(musician=pk)

    context = {
        'musician': musician,
        'musician_instruments': musician_instruments
    }

    return render(request, 'instruments/edit_musician_instruments.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_artist_genres(request, pk):
    artist = Artist.objects.get(pk=pk)

    artist_genres = ArtistGenres.objects.filter(artist=pk)

    context = {
        'artist': artist,
        'artist_genres': artist_genres,
    }
    return render(request, 'genres/edit_artist_genres.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_artist_genres(request, pk):
    artist = Artist.objects.get(pk=pk)
    artist_genres = ArtistGenres.objects.filter(artist=artist)

    if request.method == 'POST':
        form = ArtistGenresForm(request.POST, request.FILES, initial={'artist': artist})
        if form.is_valid():
            form.save()
            return redirect('artist details', pk=artist.id)
    else:
        form = ArtistGenresForm(initial={'artist': artist})
        for genre in artist_genres:
            form.fields['genre'].queryset = Genre.objects.exclude(artistgenres=genre)

    context = {
        'form': form,
        'artist': artist
    }

    return render(request, 'genres/add_artist_genres.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
def edit_artist_albums(request, pk):
    artist = Artist.objects.get(pk=pk)

    artist_albums = Album.objects.filter(artist=pk)

    context = {
        'artist': artist,
        'artist_albums': artist_albums,
    }
    return render(request, 'albums/edit-artist-albums.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    reviews = Review.objects.filter(album=album.id)
    songs = Song.objects.filter(album=album.id)
    has_review = False

    if request.user.id:
        user = Profile.objects.get(pk=request.user.id)
        for review in reviews:
            if review.user == user:
                has_review = True
                break
    else:
        has_review = False

    context = {
        'album': album,
        'reviews': reviews,
        'songs': songs,
        'has_review': has_review
    }
    return render(request, 'albums/album-details.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
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


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_song_details(request, pk):
    song = Song.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditSongForm(request.POST, request.FILES, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = EditAlbumForm(instance=song)
    context = {
        'form': form,
        'song': song,
    }
    return render(request, 'songs/edit_song_details.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_artist(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == 'POST':
        artist.delete()
        return redirect('home')
    else:
        context = {
            'artist': artist,
        }
        return render(request, 'artists/delete-artist.html', context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_artist_album(request, pk):
    artist_album = Album.objects.get(pk=pk)

    artist_album.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_band_member(request, bk, mk):
    band_member = BandMembers.objects.get(band=bk, member=mk)

    band_member.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@user_passes_test(lambda u: u.is_staff)
def remove_band_member(request, bk, mk):
    band_member = BandMembers.objects.get(band=bk, member=mk)

    band_member.present_member = False
    band_member.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_artist_genre(request, ak, gk):
    artist_genre = ArtistGenres.objects.get(artist=ak, genre=gk)

    artist_genre.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_musician_instrument(request, mk, bk, ik):
    musician_instrument = MusicianInstruments.objects.get(musician=mk, band=bk, instrument=ik)

    musician_instrument.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_album_song(request, pk):
    song = Song.objects.get(pk=pk)

    song.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_review(request, pk):
    album = Album.objects.get(pk=pk)
    user = Profile.objects.get(pk=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album details', pk=album.id)
    else:
        form = ReviewForm(initial={'album': album, 'user': user})
    context = {
        'form': form,
        'album': album
    }

    return render(request, 'reviews/new-review.html', context)


@login_required
def edit_review(request, rk):
    review = Review.objects.get(pk=rk)
    if request.method == 'POST':
        form = EditReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditReviewForm(instance=review)
    context = {
        'form': form,
        'review': review
    }
    return render(request, 'reviews/edit-review.html', context)


def reviews(request, pk):
    reviews = Review.objects.filter(album=pk)
    album = Album.objects.get(pk=pk)

    context = {
        'reviews': reviews,
        'album': album
    }
    return render(request, 'reviews/reviews.html', context)


@login_required
def delete_review(request, pk):
    review = Review.objects.get(pk=pk)

    review.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def song_lyrics(request, pk):
    song = Song.objects.get(pk=pk)

    context = {
        'song_lyrics': song.lyrics,
    }
    return render(request, 'songs/song_lyrics.html', context)


def all_reviews(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/all_reviews.html', context)
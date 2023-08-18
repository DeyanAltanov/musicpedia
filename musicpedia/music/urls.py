from django.urls import path

from musicpedia.music.views import home, add_label, \
    add_genre, add_instrument, artists, by_letter, edit_band_members, \
    add_band_member, add_musician_instrument, add_artist, artist_details, edit_artist_info, edit_artist_genres, \
    add_artist_genres, add_album, edit_artist_albums, album_details, edit_album_info, edit_album_songs, add_album_song, \
    delete_artist, delete_artist_album, delete_band_member, delete_artist_genre, edit_musician_instruments, \
    delete_musician_instrument, edit_song_details, delete_album_song

urlpatterns = [
    path('', home, name='home'),
    path('add_artist/', add_artist, name='add artist'),
    path('add_label/', add_label, name='add label'),
    path('add_genre/', add_genre, name='add genre'),
    path('add_instrument/', add_instrument, name='add instrument'),
    path('artists/', artists, name='artists'),
    path('artists/<letter>', by_letter, name='by letter'),
    path('artist_details/<int:pk>', artist_details, name='artist details'),
    path('edit_artist_info/<int:pk>', edit_artist_info, name='edit artist info'),
    path('edit_band_members/<int:pk>', edit_band_members, name='edit band members'),
    path('add_band_member/<int:pk>', add_band_member, name='add band member'),
    path('add_musician_instrument/<int:pk>', add_musician_instrument, name='add musician instrument'),
    path('edit_musician_instruments/<int:pk>', edit_musician_instruments, name='edit musician instruments'),
    path('delete_musician_instrument/<int:mk>/<int:bk>/<int:ik>/', delete_musician_instrument, name='delete musician instrument'),
    path('edit_artist_genres/<int:pk>', edit_artist_genres, name='edit artist genres'),
    path('add_artist_genres/<int:pk>', add_artist_genres, name='add artist genres'),
    path('add_album/<int:pk>', add_album, name='add album'),
    path('edit_artist_albums/<int:pk>', edit_artist_albums, name='edit artist albums'),
    path('album_details/<int:pk>', album_details, name='album details'),
    path('edit_album_info/<int:pk>', edit_album_info, name='edit album info'),
    path('edit_album_songs/<int:pk>', edit_album_songs, name='edit album songs'),
    path('add_album_song/<int:pk>', add_album_song, name='add album song'),
    path('edit_song_details/<int:pk>', edit_song_details, name='edit song details'),
    path('delete_artist/<int:pk>', delete_artist, name='delete artist'),
    path('delete_artist_album/<int:pk>', delete_artist_album, name='delete artist album'),
    path('delete_band_member/<int:bk>/<int:mk>', delete_band_member, name='delete band member'),
    path('delete_artist_genre/<int:ak>/<int:gk>', delete_artist_genre, name='delete artist genre'),
    path('delete_album_song/<int:pk>', delete_album_song, name='delete album song')
]
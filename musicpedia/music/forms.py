from django import forms

from musicpedia.music.models import Label, Genre, ArtistGenres, BandMembers, \
    Instrument, Song, Album, MusicianInstruments, Artist


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class ArtistGenresForm(forms.ModelForm):
    class Meta:
        model = ArtistGenres
        fields = '__all__'


class BandMembersForm(forms.ModelForm):
    class Meta:
        model = BandMembers
        fields = '__all__'


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'released': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

        widgets = {
            'released': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class EditArtistForm(ArtistForm):
    def save(self, commit=True):
        band = Artist.objects.get(pk=self.instance.id)
        return super().save(commit)

    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class MusicianInstrumentsForm(forms.ModelForm):
    class Meta:
        model = MusicianInstruments
        fields = '__all__'


class EditAlbumForm(AlbumForm):
    def save(self, commit=True):
        album = Album.objects.get(pk=self.instance.id)
        return super().save(commit)

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
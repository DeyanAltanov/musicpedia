from django import forms

from musicpedia.music.models import Label, Genre, ArtistGenres, BandMembers, \
    Instrument, Song, Album, MusicianInstruments, Artist, Review


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = '__all__'


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

        widgets = {
            'born': forms.widgets.DateInput(attrs={'type': 'date'})
        }


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

    def __init__(self, *args, **kwargs):
        super(BandMembersForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = Artist.objects.filter(is_band=False)


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

    def __init__(self, *args, **kwargs):
        super(MusicianInstrumentsForm, self).__init__(*args, **kwargs)
        self.fields['band'].queryset = Artist.objects.filter(is_band=True)


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


class EditSongForm(SongForm):
    def save(self, commit=True):
        song = Song.objects.get(pk=self.instance.id)
        return super().save(commit)

    class Meta:
        model = Song
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'album': forms.HiddenInput(),
            'date': forms.HiddenInput()
        }


class EditReviewForm(ReviewForm):
    def save(self, commit=True):
        review = Review.objects.get(pk=self.instance.id)
        return super().save(commit)

    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
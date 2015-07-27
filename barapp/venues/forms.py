from django import forms
from . models import Venue


class VenueCreateForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ['name', 'direction', 'phone_number', 'description', 'image']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(VenueCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        venue = super(VenueCreateForm, self).save(commit=False)
        venue.user = self.user
        if commit:
            venue.save()
        return venue


class VenueUpdateForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ['name', 'direction', 'phone_number', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(VenueUpdateForm, self).__init__(*args, **kwargs)

from django import forms
from . models import Venue


class VenueCreateForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ['name', 'direction', 'phone_number', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(VenueCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data


class VenueUpdateForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ['name', 'direction', 'phone_number', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(VenueUpdateForm, self).__init__(*args, **kwargs)
        try:
            venue = Venue.objects.get(
                id=kwargs['instance'].id
            )
        except Venue.DoesNotExist:
            raise forms.ValidationError(
                'The venue "%(venue)s" does not exist',
                code='invalid_venue',
                params={
                    'venue': kwargs['instance'].name
                }
            )
        self.initial.update({
            'name': venue.name,
            'description': venue.description,
        })

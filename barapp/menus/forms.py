from django import forms
from . models import Menu


class MenuCreateForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        self.venue = kwargs.pop('venue')
        super(MenuCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        menu = super(MenuCreateForm, self).save(commit=False)
        menu.venue = self.venue
        if commit:
            menu.save()
        return menu


class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu

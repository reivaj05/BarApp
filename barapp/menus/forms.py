from django import forms
from . models import Menu


class MenuCreateForm(forms.ModelForm):

    class Meta:
        model = Menu

    def __init__(self, *args, **kwargs):
        super(MenuCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        return self.cleaned_data


class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu

    def __init__(self, *args, **kwargs):
        super(MenuUpdateForm, self).__init__(*args, **kwargs)
        try:
            menu = Menu.objects.get(
                id=kwargs['instance'].id
            )
        except Menu.DoesNotExist:
            raise forms.ValidationError(
                'The menu "%(menu)s" does not exist',
                code='invalid_menu',
                params={
                    'menu': kwargs['instance'].name
                }
            )
        self.initial.update({
            'name': menu.name,
            'description': menu.description,
        })

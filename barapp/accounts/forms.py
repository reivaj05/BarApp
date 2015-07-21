from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from accounts import models, validators


class UserProfileCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirm password'
        )

    class Meta:
        model = User
        fields = [
            'username', 'password', 'confirm_password', 'first_name',
            'last_name', 'email'
            ]
        labels = {
            'email': 'Email address'
        }
        widgets = {
            'password': forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(
            validators.validate_username_does_not_exists)
        self.fields['username'].help_text = ''
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'password',
                    forms.ValidationError(
                        'Passwords does not match',
                        code='password_mismatch'
                        )
                    )
                self.add_error(
                    'confirm_password',
                    forms.ValidationError(
                        'Passwords does not match',
                        code='password_mismatch'
                        )
                    )
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserProfileCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            models.UserProfile.objects.create(authentication_user=user)
        return user


class UserProfileUpdateForm(forms.ModelForm):
    image_profile = forms.ImageField(
        required=False, label='Profile image'
        )
    age = forms.IntegerField(label='Age', required=True)
    gender = forms.ChoiceField(
        label='Gender',
        required=True,
        choices=models.UserProfile.GENDER_CHOICES)
    bio = forms.CharField(
        required=True,
        widget=forms.Textarea)
    is_smoker = forms.BooleanField(required=False)
    is_drinker = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'age', 'gender', 'is_smoker',
            'is_drinker', 'email', 'image_profile', 'bio'
            ]
        labels = {
            'email': 'Email address'
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        try:
            user_profile = models.UserProfile.objects.get(
                authentication_user=kwargs['instance']
                )
        except UserProfile.DoesNotExist:
            raise ValidationError(
                'The username "%(username)s" does not have a related UserProfile',
                code='invalid_username',
                params={
                    'username': kwargs['instance'].username
                }
                )
        self.initial.update({
            'image_profile': user_profile.image_profile,
            'age': user_profile.age,
            'gender': user_profile.gender,
            'bio': user_profile.bio,
            'is_smoker': user_profile.is_smooker,
            'is_drinker': user_profile.is_drinker
        })

    def save(self, commit=True):
        user = super(UserProfileUpdateForm, self).save(commit=False)
        user_profile = models.UserProfile.objects.get(authentication_user=user)
        user_profile.age = self.cleaned_data['age']
        user_profile.gender = self.cleaned_data['gender']
        user_profile.image_profile = self.cleaned_data['image_profile']
        user_profile.bio = self.cleaned_data['bio']
        user_profile.is_smooker = self.cleaned_data['is_smoker']
        user_profile.is_drinker = self.cleaned_data['is_drinker']
        if commit:
            user_profile.save()
            user.save()
        return user


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Username',
        validators=[
            validators.validate_user_already_exists,
            validators.validate_user_is_active
            ]
        )
    password = forms.CharField(
        max_length=128, widget=forms.PasswordInput,
        label='Password'
        )
    next_url = forms.CharField(
        max_length=128, required=False, widget=forms.HiddenInput
        )

    def is_valid(self):
        is_valid = super(AuthenticationForm, self).is_valid()
        if is_valid:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user_authenticated = authenticate(
                username=username, password=password
                )
            if user_authenticated is None:
                self.add_error(
                    'password',
                    forms.ValidationError(
                        'Incorrect password',
                        code='incorrect_password'
                        )
                    )
                is_valid = False
            else:
                self.cleaned_data['user_authenticated'] = user_authenticated
        return is_valid

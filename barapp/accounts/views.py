from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import (
    CreateView, DetailView, FormView,
    RedirectView, TemplateView, UpdateView,
)
from django.utils.translation import ugettext_lazy as _
from .forms import (
    AuthenticationForm, UserProfileCreateForm,
    UserProfileUpdateForm,
)
from .models import UserProfile
from common.mixins import FormMessagesMixin, LoginRequiredMixin

# Create your views here.


class IndexView(TemplateView):
    template_name = 'accounts/index.html'


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/detail_user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        authentication_user = self.request.user
        return UserProfile.objects.get(
            authentication_user=authentication_user
        )


class UserProfileCreateView(FormMessagesMixin, CreateView):
    form_class = UserProfileCreateForm
    template_name = 'accounts/create_user_profile.html'
    success_message = _('User profile successfully created')
    error_message = _('There was an error trying to create the user profile')

    def get_success_url(self):
        return reverse('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            user_profile_url = reverse('accounts:user_profile')
            return redirect(user_profile_url)
        else:
            return super(
                UserProfileCreateView, self).get(request, *args, **kwargs)


class UserProfileUpdateView(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    form_class = UserProfileUpdateForm
    template_name = 'accounts/update_user_profile.html'
    success_message = _('User profile successfully updated')
    error_message = _('An error ocurred trying to update the user profile')

    def get_success_url(self):
        return reverse('accounts:user_profile')

    def get_form_kwargs(self):
        kwargs = super(UserProfileUpdateView, self).get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs

    def get_object(self, queryset=None):
        authentication_user = self.request.user
        return UserProfile.objects.get(
            authentication_user=authentication_user
        )


class LoginFormView(FormMessagesMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_message = _('User successfully logged in')
    error_message = _('There was an error trying to log in')

    def __init__(self, **kwargs):
        self.success_url = reverse('accounts:user_profile')

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user_authenticated'])
        return super(LoginFormView, self).form_valid(form)

    def get_success_url(self):
        success_url = super(LoginFormView, self).get_success_url()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            next_url = form.cleaned_data['next_url']
            if next_url:
                return next_url
        return success_url

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.add_message(
                request=request, level=messages.INFO,
                message=_('Already logged in')
            )
            return redirect(self.get_success_url())
        return super(LoginFormView, self).get(request, *args, **kwargs)

    def get_initial(self):
        initial = super(LoginFormView, self).get_initial()
        next_url = self.request.GET.get('next')
        initial = {
            'next_url': next_url
        }
        return initial


class LogoutRedirectView(RedirectView):
    permanent = False
    pattern_name = 'common:index'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
            messages.add_message(
                request=request, level=messages.SUCCESS,
                message=_('Logout successful')
            )
        else:
            messages.add_message(
                request=request, level=messages.ERROR,
                message=_('There is no user logged in')
            )
        return super(LogoutRedirectView, self).get(request, *args, **kwargs)

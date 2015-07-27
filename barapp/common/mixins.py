from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect


class FormMessagesMixin(object):

    success_message = None
    error_message = None

    def form_valid(self, form):
        if self.success_message:
            messages.add_message(
                request=self.request,
                level=messages.SUCCESS,
                message=self.success_message
                )
        else:
            raise ImproperlyConfigured(
                '"success_message" field must be defined'
                )
        return super(FormMessagesMixin, self).form_valid(form)

    def form_invalid(self, form):
        if self.error_message:
            messages.add_message(
                request=self.request,
                level=messages.ERROR,
                message=self.error_message
                )
        else:
            raise ImproperlyConfigured(
                '"error_message" field must be defined'
                )
        return super(FormMessagesMixin, self).form_invalid(form)


class LoginRequiredMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            messages.add_message(
                request=self.request,
                level=messages.INFO,
                message='Please login to access that view'
                )
            return redirect_to_login(next=request.get_full_path())
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class PermissionRequiredMixin(View):
    permission = None

    def __init__(self, **kwargs):
        self.no_permission_url = reverse('accounts:user_profile')

    def dispatch(self, request, *args, **kwargs):
        if self.permission:
            if request.user.has_perm(self.permission):
                return super(PermissionRequiredMixin, self).dispatch(
                    request, *args, **kwargs)
            else:
                messages.add_message(
                    request=self.request,
                    level=messages.INFO,
                    message='You do not have permission for this action'
                )
                return redirect(self.no_permission_url)
        else:
            raise ImproperlyConfigured(
                '"permission" field must be defined'
            )


class DoesExistMixin(View):
    model = None

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(DoesExistMixin, self).dispatch(
                request, *args, **kwargs)
        except self.model.DoesNotExist:
            raise Http404

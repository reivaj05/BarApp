from django.views import generic
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login


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


class LoginRequiredMixin(generic.View):

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

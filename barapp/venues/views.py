from django.views.generic import (
    CreateView, DetailView, DeleteView,
    ListView, TemplateView, UpdateView,
)
from django.core.urlresolvers import reverse
from django.http import Http404
from .forms import VenueCreateForm, VenueUpdateForm
from .models import Venue
from common.mixins import (
    FormMessagesMixin, LoginRequiredMixin, PermissionRequiredMixin
)

# Create your views here.


class IndexView(TemplateView):
    template_name = 'venues/index.html'


class VenueListView(LoginRequiredMixin, ListView):
    template_name = 'venues/venue_list.html'
    context_object_name = 'venue_list'
    model = Venue


class VenueDetailView(LoginRequiredMixin, DetailView):
    template_name = 'venues/venue_detail.html'
    model = Venue


class VenueDeleteView(
        LoginRequiredMixin, PermissionRequiredMixin,
        FormMessagesMixin, DeleteView):
    template_name = 'venues/venue_delete.html'
    model = Venue
    permission = 'venues.delete_venue'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(VenueDeleteView, self).dispatch(
                request, *args, **kwargs)
        except Venue.DoesNotExist:
            raise Http404

    def get_success_url(self):
        return reverse('venues:venue_list')


class VenueCreateView(
        LoginRequiredMixin, PermissionRequiredMixin,
        FormMessagesMixin, CreateView):
    template_name = 'venues/venue_create.html'
    form_class = VenueCreateForm
    permission = 'venues.add_venue'
    success_message = 'Venue successfully created'
    error_message = 'There was an error trying to create the venue'

    def __init__(self, **kwargs):
        self.success_url = reverse('venues:venue_list')


class VenueUpdateView(
        LoginRequiredMixin, PermissionRequiredMixin,
        FormMessagesMixin, UpdateView):
    template_name = 'venues/venue_update.html'
    form_class = VenueUpdateForm
    model = Venue
    permission = 'venues.change_venue'
    success_message = 'venue successfully updated'
    error_message = 'An error ocurred trying to update the venue'

    def get_success_url(self):
        return reverse('venues:venue_detail', kwargs={'pk': self.kwargs['pk']})

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(VenueUpdateView, self).dispatch(
                request, *args, **kwargs)
        except Venue.DoesNotExist:
            raise Http404

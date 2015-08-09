from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DetailView, DeleteView,
    ListView, TemplateView, UpdateView,
)
from .forms import VenueCreateForm, VenueUpdateForm
from .models import Venue
from common.mixins import (
    FormMessagesMixin, DoesExistMixin,
    LoginRequiredMixin, PermissionRequiredMixin
)

# Create your views here.


class IndexView(TemplateView):
    template_name = 'venues/index.html'


class VenueCreateView(
        LoginRequiredMixin, PermissionRequiredMixin,
        FormMessagesMixin, CreateView):
    template_name = 'venues/venue_create.html'
    form_class = VenueCreateForm
    permission = 'venues.add_venue'
    no_permission_url = reverse_lazy('venues:venue_list')
    success_message = 'Venue successfully created'
    error_message = 'There was an error trying to create the venue'

    def __init__(self, **kwargs):
        self.success_url = reverse('venues:venue_list')

    def get_form_kwargs(self):
        kwargs = super(VenueCreateView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class VenueDeleteView(
        LoginRequiredMixin, DoesExistMixin, PermissionRequiredMixin,
        FormMessagesMixin, DeleteView):
    template_name = 'venues/venue_delete.html'
    model = Venue
    permission = 'venues.delete_venue'
    no_permission_url = reverse_lazy('venues:venue_list')
    success_message = 'venue successfully deleted'
    error_message = 'An error ocurred trying to delete the venue'

    def get_success_url(self):
        return reverse('venues:venue_list')


class VenueUpdateView(
        LoginRequiredMixin, DoesExistMixin, PermissionRequiredMixin,
        FormMessagesMixin, UpdateView):
    template_name = 'venues/venue_update.html'
    form_class = VenueUpdateForm
    model = Venue
    permission = 'venues.change_venue'
    no_permission_url = reverse_lazy('venues:venue_list')
    success_message = 'venue successfully updated'
    error_message = 'An error ocurred trying to update the venue'

    def get_success_url(self):
        return reverse('venues:venue_detail', kwargs={'pk': self.kwargs['pk']})


class VenueDetailView(
        LoginRequiredMixin, DoesExistMixin, DetailView):
    template_name = 'venues/venue_detail.html'
    model = Venue


class VenueListView(LoginRequiredMixin, ListView):
    template_name = 'venues/venue_list.html'
    context_object_name = 'venue_list'
    model = Venue

    def get_queryset(self):
        return Venue.objects.filter(user=self.request.user)

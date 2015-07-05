from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .forms import VenueCreateForm, VenueUpdateForm
from .models import Venue
from common import mixins

# Create your views here.


class IndexView(TemplateView):
    template_name = 'venues/index.html'


class VenueDetailView(DetailView):
    template_name = 'venues/detail_venue.html'
    model = Venue


class VenueCreateView(mixins.FormMessagesMixin, CreateView):
    template_name = 'venues/venue_create.html'
    form_class = VenueCreateForm
    success_message = 'Venue successfully created'
    error_message = 'There was an error trying to create the venue'


class VenueUpdateView(mixins.FormMessagesMixin, UpdateView):
    template_name = 'venues/venue_update.html'
    form_class = VenueUpdateForm
    success_message = 'venue successfully updated'
    error_message = 'An error ocurred trying to update the venue'

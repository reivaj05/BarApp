from django.conf.urls import patterns, url
from .views import IndexView, VenueCreateView, VenueDetailView, VenueUpdateView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^venue-detail/$', VenueDetailView.as_view(), name='venue_detail'),
    url(r'^venue-create/$', VenueCreateView.as_view(), name='venue_create'),
    url(r'^venue-update/$', VenueUpdateView.as_view(), name='venue_update'),
)

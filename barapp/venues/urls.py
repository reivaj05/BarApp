from django.conf.urls import url
from .views import (
    IndexView, VenueCreateView, VenueListView,
    VenueDetailView, VenueUpdateView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^venue-list/$', VenueListView.as_view(), name='venue_list'),
    url(r'^venue-create/$', VenueCreateView.as_view(), name='venue_create'),
    url(
        r'^venue-detail/(?P<pk>[0-9]+)/$',
        VenueDetailView.as_view(),
        name='venue_detail'
    ),
    url(
        r'^venue-update/(?P<pk>[0-9]+)/$',
        VenueUpdateView.as_view(),
        name='venue_update'
    ),
    url(
        r'^venue-delete/(?P<pk>[0-9]+)/$',
        VenueUpdateView.as_view(),
        name='venue_delete'
    ),
]

from django.conf.urls import patterns, url
from .views import IndexView, MenuCreateView, MenuDetailView, MenuUpdateView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^menu-detail/$', MenuDetailView.as_view(), name='menu_detail'),
    url(r'^menu-create/$', MenuCreateView.as_view(), name='menu_create'),
    url(r'^menu-update/$', MenuUpdateView.as_view(), name='menu_update'),
)

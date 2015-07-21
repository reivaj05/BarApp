from django.conf.urls import include, url, static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('common.urls', namespace='common')),
    url(r'^menus/', include('menus.urls', namespace='menus')),
    url(r'^venues/', include('venues.urls', namespace='venues')),
]

if settings.DEBUG:
    urlpatterns += static.static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

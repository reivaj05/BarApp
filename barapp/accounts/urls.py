from django.conf.urls import url
from accounts import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutRedirectView.as_view(), name='logout'),
    url(r'^user-profile/$', views.UserProfileDetailView.as_view(),
        name='user_profile'),
    url(r'^create-user-profile/$', views.UserProfileCreateView.as_view(),
        name='create_user_profile'),
    url(r'^update-user-profile/$', views.UserProfileUpdateView.as_view(),
        name='update_user_profile'),
]

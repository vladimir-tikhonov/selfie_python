from django.conf.urls import url
from user_profile.views.user_profile_view import UserProfileView

app_name = 'user_profile'
urlpatterns = [
    url(r'^(?P<username>\w+)$', UserProfileView.as_view(), name='profile'),
]

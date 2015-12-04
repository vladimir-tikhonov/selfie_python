from django.conf.urls import url

from registration.views.registration_view import RegistrationView

app_name = 'registration'
urlpatterns = [
    url(r'$', RegistrationView.as_view(), name='new')
]

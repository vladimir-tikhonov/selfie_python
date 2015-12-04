from django.conf.urls import url

from login.views.login_view import LoginView

app_name = 'login'
urlpatterns = [
    url(r'$', LoginView.as_view(), name='new')
]

from django.conf.urls import url

from home.views.home_view import HomeView

app_name = 'home'
urlpatterns = [
    url(r'', HomeView.as_view(), name='index')
]

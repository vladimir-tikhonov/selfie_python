from django.conf.urls import url

from logout.views.logout_view import LogoutView

app_name = 'logout'
urlpatterns = [
    url(r'$', LogoutView.as_view(), name='perform')
]

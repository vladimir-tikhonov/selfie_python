from django.conf.urls import url

from posts.views import PostView

app_name = 'post'
urlpatterns = [
    url(r'new$', PostView.as_view(), name='new')
]

from django.conf.urls import url
from feed.views import FeedView

app_name = 'feed'
urlpatterns = [
    url(r'^$', FeedView.as_view(), name='index'),
]

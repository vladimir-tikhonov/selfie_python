from django.conf.urls import url
from feed.views.feed_view import FeedView

app_name = 'feed'
urlpatterns = [
    url(r'^$', FeedView.as_view(), name='index'),
]

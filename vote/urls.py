from django.conf.urls import url

from vote.views.vote_view import VoteView

app_name = 'vote'
urlpatterns = [
    url(r'new$', VoteView.as_view(), name='new')
]

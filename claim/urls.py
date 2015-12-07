from django.conf.urls import url

from claim.views.claim_view import ClaimView

app_name = 'claim'
urlpatterns = [
    url(r'(?P<post_id>\d+)/new$', ClaimView.as_view(), name='new')
]

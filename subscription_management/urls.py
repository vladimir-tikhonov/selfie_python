from django.conf.urls import url
from subscription_management.views.subscription_list_view import SubscriptionListView
from subscription_management.views.subscription_view import SubscriptionView

app_name = 'subscription_management'
urlpatterns = [
    url(r'^list$', SubscriptionListView.as_view(), name='list'),
    url(r'^(?P<subscription_id>\d+)$', SubscriptionView.as_view(), name='details'),
]

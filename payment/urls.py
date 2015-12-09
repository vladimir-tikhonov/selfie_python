from django.conf.urls import url
from payment.views.payment_view import PaymentView

app_name = 'payment'
urlpatterns = [
    url(r'^(?P<username>\w+)/(?P<plan_id>\d+)/new$', PaymentView.as_view(), name='new'),
]

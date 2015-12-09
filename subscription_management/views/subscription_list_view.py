from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from subscription.models.subscription import Subscription

class SubscriptionListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    context_object_name = 'subscriptions'
    template_name = 'subscription_management/subscription_list.html'
    model = Subscription

    def get_queryset(self):
        all_subscriptions = Subscription.objects.all().order_by('id')
        queryset = []
        for subscription in all_subscriptions:
            subscription_data = {
                'customer': subscription.customer,
                'transaction': subscription.transaction,
                'status': settings.STATUS_NAMES[subscription.status],
                'link': subscription.id
            }
            queryset.append(subscription_data)
        return queryset

    def test_func(self):
        return self.request.user.role >= settings.USER_ROLE

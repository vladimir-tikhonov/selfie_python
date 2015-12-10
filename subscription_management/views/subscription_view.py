from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from subscription.models.subscription import Subscription

class SubscriptionView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'subscription_management/subscription_page.html'

    def get(self, request, subscription_id):
        subscription = Subscription.objects.get(id=subscription_id)

        return render(request, self.template_name, {'subscription': subscription})

    def post(self, request, subscription_id):
        return self.change_subscription_status(request, subscription_id)

    def test_func(self):
        return self.request.user.role >= settings.USER_ROLE

    def change_subscription_status(self, request, subscription_id):
        subscription = Subscription.objects.get(id=subscription_id)
        subscription.status = request.POST['status']
        subscription.save()
        return HttpResponseRedirect(reverse('subscription_management:list'))

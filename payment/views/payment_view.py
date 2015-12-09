from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from payment.forms.payment_form import PaymentForm
from payment.adapters.payment_adapter import PaymentAdapter
from subscription.models.subscription import Subscription
from user.models import User
from plan.models.plan import Plan


class PaymentView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = PaymentForm
    details_template_name = 'payment/payment_details.html'

    def get(self, request, username, plan_id):
        form = self.form_class()

        return render(request, PaymentAdapter.get_payment_page(),
                      {'form': form, 'plan_id': plan_id})

    def post(self, request, username, plan_id):
        subscribee = User.objects.get(username=username)
        plan = Plan.objects.get(id=plan_id)
        customer = self.request.user

        payment = PaymentAdapter.create_payment(plan, customer, subscribee)
        transaction = payment.process()
        subscription = Subscription(plan=plan, customer=customer, subscribee=subscribee, transaction=transaction)
        subscription.save()

        return render(request, self.details_template_name, {'payment': payment, 'subscription': subscription})

    def test_func(self):
        user_role = self.request.user.role
        return user_role == 0 or user_role == 1

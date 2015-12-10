from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from user.models import User

class UserView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'user_management/user_page.html'

    def get(self, request, username):
        user = User.objects.get(username=username)

        return render(request, self.template_name, {'user': user})

    def post(self, request, username):
        return self.set_as_admin(request, username)

    def test_func(self):
        return self.request.user.role > settings.MODERATOR_ROLE

    def set_as_admin(self, request, username):
        user = User.objects.get(username=username)
        user.role = settings.ADMIN_ROLE
        user.save()
        return HttpResponseRedirect(reverse('user_management:list'))

    def set_as_moderator(self):
        pass

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User

class UserProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'user_profile/profile_page.html'

    def get(self, request, username):
        return self.view_profile(request, username)

    def view_profile(self, request, username):
        user = User.objects.get(username=username)

        return render(request, self.template_name, {'user': user})

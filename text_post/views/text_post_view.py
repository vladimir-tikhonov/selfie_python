from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class PostView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'text_post/new.html'

    def post(self, request):
        pass

    def test_func(self):
        pass

    def add_text_post(self, request):
        pass

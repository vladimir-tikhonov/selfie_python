from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class FeedView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    context_object_name = 'posts'
    template_name = 'posts/recent_posts_page.html'

    def test_func(self):
        return self.request.user.role == 0

    def view_recent_posts(self):
        pass

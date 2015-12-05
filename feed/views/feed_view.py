from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models.post import Post

class FeedView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'feed/feed_page.html'

    def test_func(self):
        return self.request.user.role == 0

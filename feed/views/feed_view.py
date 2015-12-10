from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models.post import Post
from vote.forms.vote_form import VoteForm
from vote.models.vote import Vote

class FeedView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    context_object_name = 'posts'
    template_name = 'feed/feed_page.html'

    def test_func(self):
        return self.request.user.role == 0

    def get_queryset(self):
        all_posts = Post.objects.filter(claim__isnull=True)
        queryset = []
        for post in all_posts:
            post_data = {
                'id': post.id,
                'picture': post.picture,
                'current_vote': self.get_current_user_vote(post)
            }
            queryset.append(post_data)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(FeedView, self).get_context_data(**kwargs)
        context['vote_form'] = VoteForm()
        return context

    def get_current_user_vote(self, post):
        current_user = self.request.user
        vote = Vote.objects.filter(user_id=current_user.id, post_id=post.id).first()
        if vote:
            return vote.value
        else:
            return None

    def view_feed(self):
        pass

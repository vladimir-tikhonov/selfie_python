from django.views.generic import ListView
from posts.models.post import Post

class FeedView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'feed/feed_page.html'

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

from posts.models import Post
from posts.forms import PostForm

class PostView(View):
    form_class = PostForm
    template_name = 'posts/new.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(picture=request.FILES['picture'])
            new_post.save()
            return HttpResponseRedirect(reverse('feed:index'))
        else:
            return render(request, self.template_name, {'form': form})

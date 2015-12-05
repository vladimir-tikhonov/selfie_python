from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models.post import Post
from posts.forms.post_form import PostForm

class PostView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
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

    def test_func(self):
        user_role = self.request.user.role
        return user_role == 0 or user_role == 1

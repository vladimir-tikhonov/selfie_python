from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from posts.models import Post
from posts.forms import PostForm


def index(request):
    posts = Post.objects.all()

    return render(
        request,
        'posts/index.html',
        {'posts': posts}
    )

def new(request):
    form = PostForm()

    return render(
        request,
        'posts/new.html',
        {'form': form}
    )

def create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = Post(picture=request.FILES['picture'])
        new_post.save()

    return HttpResponseRedirect(reverse('posts:index'))

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from posts.models import Post
from posts.forms import PostForm


def index(request):
    posts = Post.objects.all()

    return render_to_response(
        'index.html',
        {'posts': posts},
        context_instance=RequestContext(request)
    )

def new(request):
    form = PostForm()

    return render_to_response(
        'new.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        new_post = Post(picture=request.FILES['picture'])
        new_post.save()

    return HttpResponseRedirect(reverse('posts:index'))

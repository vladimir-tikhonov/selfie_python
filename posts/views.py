from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from posts.models import Post
from posts.forms import PostForm


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = Post(picture=request.FILES['picture'])
            new_post.save()

        # Redirect to the document list after POST
        return HttpResponseRedirect(reverse('posts.views.index'))
    else:
        form = PostForm()  # A empty, unbound form

    # Load documents for the list page
    posts = Post.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'index.html',
        {'posts': posts, 'form': form},
        context_instance=RequestContext(request)
    )

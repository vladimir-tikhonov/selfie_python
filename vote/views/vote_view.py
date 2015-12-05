from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from vote.models.vote import Vote

class VoteView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request):
        vote, _ = Vote.objects.update_or_create(
            user = self.request.user,
            post_id = request.POST['post_id'],
            defaults={'value': request.POST['value']}
        )
        return HttpResponseRedirect(reverse('feed:index'))

    def test_func(self):
        user_role = self.request.user.role
        return user_role == 0 or user_role == 1

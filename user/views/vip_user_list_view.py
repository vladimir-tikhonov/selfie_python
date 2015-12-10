from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from user.models import User

class VipUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    context_object_name = 'users'
    template_name = 'user/vip_user_list.html'
    model = User

    def get_queryset(self):
        return User.objects.filter(role=settings.VIP_USER_ROLE)

    def test_func(self):
        return self.request.user.role < settings.MODERATOR_ROLE

    def view_vip_users_list(self):
        pass

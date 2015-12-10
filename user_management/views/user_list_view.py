from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from user.models import User

class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = '/login/'
    context_object_name = 'users'
    template_name = 'user_management/user_list.html'
    model = User

    def get_queryset(self):
        all_users = User.objects.filter(role__lt=settings.DIRECTOR_ROLE)
        queryset = []
        for user in all_users:
            user_data = {
                'username': user.username,
                'role': settings.ROLE_NAMES[user.role],
                'link': user.username
            }
            queryset.append(user_data)
        return queryset

    def test_func(self):
        return self.request.user.role > settings.MODERATOR_ROLE

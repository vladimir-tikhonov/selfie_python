from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    templates = ['home/user_index.html', 'home/vip_user_index.html',
                 'home/moderator_index.html', 'home/admin_index.html', 'home/director_index.html']

    def get(self, request):
        if request.user.is_authenticated():
            user_role = request.user.role
            template_name = self.templates[user_role]
            return render(request, template_name)
        else:
            return render(request, 'home/guest_index.html')

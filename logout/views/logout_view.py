from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request):
        return self.perform_logout(request)

    def perform_logout(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home:index'))

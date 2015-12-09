from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.views.generic import View
from login.forms.login_form import LoginForm

class LoginView(View):
    form_class = LoginForm
    template_name = 'login/login_page.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('home:index'))
        else:
            return render(request, self.template_name, {'form': form})

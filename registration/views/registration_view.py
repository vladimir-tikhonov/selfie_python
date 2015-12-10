from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from registration.forms.registration_form import RegistrationForm

class RegistrationView(View):
    form_class = RegistrationForm
    template_name = 'registration/registration_page.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        return self.perform_registration(request)

    def perform_registration(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login:new'))
        else:
            return render(request, self.template_name, {'form': form})

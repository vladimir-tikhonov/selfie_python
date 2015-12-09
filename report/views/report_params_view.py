from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from report.forms.report_params_form import ReportParamsForm

class ReportParamsView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = ReportParamsForm
    template_name = 'report/report_params_page.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print(request.POST)
        return HttpResponseRedirect(reverse('report:view',
                                    kwargs={'start': request.POST['start'], 'end': request.POST['end']}))

    def test_func(self):
        return self.request.user.role == 4

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from report.models.report import Report
from report.forms.report_form import ReportForm

class ReportView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    form_class = ReportForm
    template_name = 'report/new_report.html'

    def get(self, request, post_id):
        form = self.form_class()

        return render(request, self.template_name, {'form': form, 'post_id': post_id})

    def post(self, request, post_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_report = Report(reason=request.POST['reason'],
                                user=self.request.user,
                                post_id=post_id
            )
            new_report.save()
            return HttpResponseRedirect(reverse('feed:index'))
        else:
            return render(request, self.template_name, {'form': form, 'post_id': post_id})

    def test_func(self):
        user_role = self.request.user.role
        return user_role == 0 or user_role == 1

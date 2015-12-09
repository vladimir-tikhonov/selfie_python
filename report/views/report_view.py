from datetime import datetime
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from payment.adapters.payment_adapter import PaymentAdapter
from printer.adapters.printer_adapter import PrinterAdapter
from report.report import Report

class ReportView(UserPassesTestMixin, LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'report/report_page.html'

    def get(self, request, start, end):
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        transactions = PaymentAdapter.get_report_data(start, end)

        return render(request, self.template_name,
                      {'transactions': transactions, 'start': start, 'end': end})

    def post(self, request, start, end):
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        transactions = PaymentAdapter.get_report_data(start, end)
        report = Report()
        PrinterAdapter.print_report(report)
        messages.add_message(request, messages.INFO, 'Печать отчёта запланирована.')

        return render(request, self.template_name,
                      {'transactions': transactions, 'start': start, 'end': end})

    def test_func(self):
        user_role = self.request.user.role
        return user_role == 0 or user_role == 1

from django.conf.urls import url

from report.views.report_view import ReportView

app_name = 'report'
urlpatterns = [
    url(r'(?P<post_id>\d+)/new$', ReportView.as_view(), name='new')
]

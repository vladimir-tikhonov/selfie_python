from django.conf.urls import url

from report.views.report_params_view import ReportParamsView
from report.views.report_view import ReportView

app_name = 'report'
urlpatterns = [
    url(r'new$', ReportParamsView.as_view(), name='new'),
    url(r'view/(?P<start>\d+-\d+-\d+)/(?P<end>\d+-\d+-\d+)$', ReportView.as_view(), name='view')
]

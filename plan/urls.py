from django.conf.urls import url
from plan.views.plan_list_view import PlanListView

app_name = 'plan'
urlpatterns = [
    url(r'^(?P<username>\w+)/choose$', PlanListView.as_view(), name='choose'),
]

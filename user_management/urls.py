from django.conf.urls import url
from user_management.views.user_list_view import UserListView
from user_management.views.user_view import UserView

app_name = 'user_management'
urlpatterns = [
    url(r'^list$', UserListView.as_view(), name='list'),
    url(r'^(?P<username>\w+)$', UserView.as_view(), name='details'),
]

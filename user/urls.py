from django.conf.urls import url
from user.views.vip_user_list_view import VipUserListView

app_name = 'user'
urlpatterns = [
    url(r'^vip$', VipUserListView.as_view(), name='vip_list'),
]

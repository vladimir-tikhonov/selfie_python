from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^post/', include('posts.urls')),
    url(r'^feed/', include('feed.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^vote/', include('vote.urls')),
    url(r'^claim/', include('claim.urls')),
    url(r'^users/', include('user_management.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, re_path

from core.views import base


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    re_path(r'^(?P<url_path>.*)/$', base)
]

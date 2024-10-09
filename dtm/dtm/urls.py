from django.contrib import admin
from django.urls import path

from core.views import base, start


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start),
    path('<str:menu_name>/', base),
    path('<str:menu_name>/<str:active>/', base)
]

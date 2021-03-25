from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
# from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
]
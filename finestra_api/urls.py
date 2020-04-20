from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from finestra_api import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('relat.urls'))
]

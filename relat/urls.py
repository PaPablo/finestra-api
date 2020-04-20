from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from relat.views import RelatViewSet

router = routers.SimpleRouter()
router.register('relat', RelatViewSet)


urlpatterns = [
    path('', include(router.urls))
]

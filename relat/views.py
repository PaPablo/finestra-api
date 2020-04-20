from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from relat.models import Relat
from relat.serializers import RelatSerializer


class RelatViewSet(ModelViewSet):
    queryset = Relat.objects.all()
    serializer_class = RelatSerializer

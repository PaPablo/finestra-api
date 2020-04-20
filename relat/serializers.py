from rest_framework.serializers import ModelSerializer
from relat.models import Relat


class RelatSerializer(ModelSerializer):
    class Meta:
        model = Relat
        fields = ['title']

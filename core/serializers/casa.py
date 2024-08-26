from rest_framework.serializers import ModelSerializer

from core.models import Casa

class CasaSerializer(ModelSerializer):
    class Meta:
        model = Casa
        fields = "__all__"

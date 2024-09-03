from rest_framework.serializers import ModelSerializer

from core.models import Familia

class FamiliaSerializer(ModelSerializer):
    class Meta:
        model = Familia
        fields = "__all__"

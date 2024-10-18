from rest_framework.serializers import ModelSerializer, Serializer, IntegerField

from core.models import Casa

class CasaSerializer(ModelSerializer):
    class Meta:
        model = Casa
        fields = ("id", "numero_comodos", "descricao", "numero_casa")

from rest_framework.serializers import ModelSerializer

from core.models import Prontuario

class ProntuarioSerializer(ModelSerializer):
    class Meta:
        model = Prontuario
        fields = "__all__"
        depth = 1

from rest_framework.viewsets import ModelViewSet

from core.models import Prontuario
from core.serializers import ProntuarioSerializer

class ProntuarioViewSet(ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
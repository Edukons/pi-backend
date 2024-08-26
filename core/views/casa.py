from rest_framework.viewsets import ModelViewSet

from core.models import Casa
from core.serializers import CasaSerializer

class CasaViewSet(ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
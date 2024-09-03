from rest_framework.viewsets import ModelViewSet

from core.models import Familia
from core.serializers import FamiliaSerializer

class FamiliaViewSet(ModelViewSet):
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
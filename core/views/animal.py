from rest_framework.viewsets import ModelViewSet

from core.models import Animal
from core.serializers import AnimalSerializer

class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
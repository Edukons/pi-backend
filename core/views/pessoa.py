from rest_framework.viewsets import ModelViewSet

from core.models import Pessoa
from core.serializers import PessoaSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
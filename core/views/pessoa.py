from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Pessoa
from core.serializers import PessoaSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["nome","cpf"]
    search_fields = ['^nome', '^cpf']
    ordering_fields = ["nome", "cpf", "data_nasc", "status_escolaridade", "fotoPessoa"]
    ordering = ["nome"]
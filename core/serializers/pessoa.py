from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Pessoa

class PessoaSerializer(ModelSerializer):
    fotoPessoa_attachment_key = SlugRelatedField(
        source="fotoAnimal",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    fotoPessoa = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Pessoa
        fields = ("__all__")

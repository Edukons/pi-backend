from django.db import models

from uploader.models import Image
class Animal(models.Model):
    nome = models.CharField(max_length=30)
    especie = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    fotoAnimal = models.ForeignKey(
        Image,
        related_name="+",
        on_delete= models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    "fk de pessoa e prontuario aqui"
    def __str__(self):
        return f"({self.nome}) {self.especie}"
    class Meta:
        verbose_name_plural = "Animais"

from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=30)
    especie = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    foto = models.ImageField
    "fk de pessoa e prontuario aqui"
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Animais"

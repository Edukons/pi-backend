from django.db import models
from .animal import Animal

class Prontuario(models.Model):
    data_adoeceu = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=500)
    nomeAnimal = models.ForeignKey(Animal, related_name="nome", on_delete= models.SET_NULL, null=True, blank=True, default=None,)
    def __str__(self):
        return self.nomeAnimal
    
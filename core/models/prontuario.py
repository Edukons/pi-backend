from django.db import models
from .animal import Animal

class Prontuario(models.Model):
    data_adoeceu = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=500)
    animal = models.ForeignKey(Animal, related_name="prontuarios", on_delete= models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.animal.nome
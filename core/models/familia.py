from django.db import models
from .pessoa import Pessoa
from .casa import Casa

class Familia(models.Model):
    pessoas = models.ManyToManyField(Pessoa, related_name="pessoas", blank=True)
    casa = models.ForeignKey(Casa, on_delete=models.PROTECT, related_name="casa", null=True, blank=True)
    def __str__(self):
        return f"Casa {self.casa.numero_casa}"
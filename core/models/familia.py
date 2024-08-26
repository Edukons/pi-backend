from django.db import models
from .pessoa import Pessoa
from .casa import Casa

class Familia(models.Model):
    pessoas = models.ForeignKey(Pessoa, on_delete=models.PROTECT, related_name="pessoas", null=True, blank=True)
    casa = models.ForeignKey(Casa, on_delete=models.PROTECT, related_name="casa", null=True, blank=True)
    def __str__(self):
        return self.pessoas
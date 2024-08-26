from django.db import models

class Casa(models.Model):
    numero_casa = models.CharField(max_length=6)
    numero_comodos = models.CharField(max_length=2)
    data_entrada = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=500)
    def __str__(self):
        return self.numero_casa
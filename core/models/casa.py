from django.db import models

class Casa(models.Model):
    numero_casa = models.DecimalField
    numero_comodos = models.DecimalField
    data_entrada = models.DateField
    descricao = models.CharField(max_length=500)
    def __str__(self):
        return self.descricao
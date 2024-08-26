from django.db import models

class Prontuario(models.Model):
    nome = models.CharField(max_length=30)
    data_adoeceu = models.DateField(blank=True, null=True)
    descricao = models.CharField(max_length=500)
    def __str__(self):
        return self.nome
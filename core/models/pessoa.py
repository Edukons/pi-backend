from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9, blank=True, null=True)
    cpf = models.CharField(max_length=15)
    data_nasc = models.DateField(blank=True, null=True)
    foto = models.ImageField
    class StatusEscolaridade(models.IntegerChoices):
            NENHUMA = 1, "Nenhuma"
            FUNDAMENTAL_INCOMPLETO = 2, "Fundamental Incompleto"
            FUNDAMENTAL_COMPLETO = 3, "Fundamental Completo"
            ENSINO_MEDIO_INCOMPLETO = 4, "Ensino Médio Incompleto"
            ENSINO_MEDIO_COMPLETO = 5, "Ensino Médio Completo"
            SUPERIOR_INCOMPLETO = 6, "Ensino Superior Incompleto"
            SUPERIOR_COMPLETO = 7, "Ensino Superior Completo"
            OUTRO = 8, "Outro"
    status_escolaridade = models.IntegerField(choices=StatusEscolaridade.choices, default=1)
    def __str__(self):
        return self.nome


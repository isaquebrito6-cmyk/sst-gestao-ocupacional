from django.db import models
from colaboradores.models import Colaborador

class PCMSO(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    validade = models.DateField()
    arquivo = models.CharField(max_length=255)  # URL do Firebase Storage

    def __str__(self):
        return f"PCMSO - {self.colaborador.nome}"

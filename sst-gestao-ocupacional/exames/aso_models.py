from django.db import models
from .models import Exame

class ASO(models.Model):
    exame = models.OneToOneField(Exame, on_delete=models.CASCADE)
    validade = models.DateField()
    arquivo = models.CharField(max_length=255)  # URL do Firebase Storage

    def __str__(self):
        return f"ASO - {self.exame.colaborador.nome}"

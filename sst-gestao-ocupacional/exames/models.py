from django.db import models
from colaboradores.models import Colaborador
from clinicas.models import Clinica

class Exame(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.colaborador.nome}"

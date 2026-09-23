from django.db import models

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

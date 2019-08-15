from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
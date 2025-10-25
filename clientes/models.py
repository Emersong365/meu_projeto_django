from django.db import models
from app.models import Produto

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
from django.db import models

# Create your models here.

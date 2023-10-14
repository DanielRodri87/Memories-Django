from django.db import models

# Create your models here.
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    tag = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

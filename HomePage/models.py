from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    nome = models.CharField(max_length=12, unique=True)

class Produtos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='static/img/Produtos')
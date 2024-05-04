from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Tag(models.Model):
    nome = models.CharField(max_length=12, unique=True)

class Produtos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='')
    quantidade = models.PositiveIntegerField(validators=[MinValueValidator(1)])

class UserImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    imgUSER = models.ImageField(upload_to='')
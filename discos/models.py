from django.db import models

# Create your models here.
class Disco(models.Model):
    Nome = models.CharField(max_length=200)
    Descricao = models.TextField()
    Selo_fonografico = models.CharField(max_length=50)
    Ano = models.PositiveIntegerField()
    Pais = models.CharField(max_length=50)
    Genero = models.CharField(max_length=100)
    Quantidade = models.PositiveIntegerField()
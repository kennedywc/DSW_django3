from django.db import models

class Artista(models.Model):
    artista = models.CharField(max_length=100)

    def __str__(self):
        return self.artista


class SeloFonografico(models.Model):
    selo_fonografico = models.CharField(max_length=100)

    def __str__(self):
        return self.selo_fonografico



# Create your models here.
class Disco(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    selo_fonografico = models.ForeignKey(SeloFonografico, on_delete=models.CASCADE, null=True)
    ano = models.PositiveIntegerField()
    pais = models.CharField(max_length=50)
    genero = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    artista = models.ManyToManyField(Artista)

    def __str__(self):
        return self.nome
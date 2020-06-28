from django.db import models

# Create your models here.

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologia = models.CharField(max_length=20)
    imagem = models.FilePathField(path="/img")

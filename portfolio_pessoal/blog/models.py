from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=20)

class Postagem(models.Model):
    titulo = models.CharField(max_length=255)
    postagem = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    ultima_alteracao = models.DateTimeField(auto_now=True)
    categoria = models.ManyToManyField("Categoria", related_name="Postagem")

class Comentario(models.Model):
    autor = models.CharField(max_length=60)
    comentario =  models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    postagem = models.ForeignKey("Postagem", on_delete=models.CASCADE)


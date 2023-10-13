from django.db import models

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)

class Residente(models.Model):
    id_residente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()

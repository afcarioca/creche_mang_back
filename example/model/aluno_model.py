from django.db import models


class AlunoModel(models.Model):
    nome = models.CharField(max_length=200)
    turma = models.CharField(max_length=20)
    bolsa_familia= models.BooleanField()
    sexo = models.CharField(max_length=20)
    ativo= models.BooleanField()
    alcool = models.BooleanField(default=0)
    jogos = models.BooleanField(default=0)


    class Meta:
        db_table ="aluno"
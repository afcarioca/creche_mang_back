from django.db import models


class AlunoModel(models.Model):
    nome = models.CharField(max_length=200)
    turma = models.CharField(max_length=20)
    bolsa_familia= models.BooleanField()
    sexo = models.CharField(max_length=20)


    class Meta:
        db_table ="aluno"
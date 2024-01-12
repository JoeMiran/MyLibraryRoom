from django.db import models


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30)
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.IntegerField(default=0)

class Meta:
    verbose_name = 'Livro'


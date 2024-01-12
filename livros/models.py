from django.db import models
from datetime import datetime 

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(blank=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True)
    data_emprestimo = models.DateTimeField(blank=True, default=datetime.now)
    data_devolucao = models.DateTimeField(blank=True)
    tempo_duracao = models.DateField(blank=True)

    class Meta:
        verbose_name = 'Livro'

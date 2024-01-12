# Generated by Django 5.0.1 on 2024-01-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('co_autor', models.CharField(max_length=30)),
                ('data_cadastro', models.DateField()),
                ('emprestado', models.BooleanField(default=False)),
                ('nome_emprestado', models.CharField(max_length=30)),
                ('data_devolucao', models.DateTimeField()),
                ('tempo_duracao', models.IntegerField(default=0)),
            ],
        ),
    ]
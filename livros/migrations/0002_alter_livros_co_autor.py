# Generated by Django 5.0.1 on 2024-01-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro'},
        ),
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

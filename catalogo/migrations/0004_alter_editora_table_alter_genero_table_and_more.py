# Generated by Django 5.1.1 on 2024-10-23 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_alter_autor_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='editora',
            table='editora',
        ),
        migrations.AlterModelTable(
            name='genero',
            table='genero',
        ),
        migrations.AlterModelTable(
            name='livro',
            table='livro',
        ),
    ]

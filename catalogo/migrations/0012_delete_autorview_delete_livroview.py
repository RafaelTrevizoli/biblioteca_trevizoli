# Generated by Django 5.1.1 on 2024-10-29 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0011_autorview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AutorView',
        ),
        migrations.DeleteModel(
            name='LivroView',
        ),
    ]

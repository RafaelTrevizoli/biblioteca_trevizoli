# Generated by Django 5.1.1 on 2024-10-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_remove_autor_data_nascimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LivroView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro_id', models.IntegerField()),
                ('livro_titulo', models.CharField(max_length=255)),
                ('autor_nome', models.CharField(max_length=255)),
                ('editora_nome', models.CharField(max_length=255)),
                ('genero_nome', models.CharField(max_length=255)),
                ('tags_nomes', models.TextField()),
            ],
            options={
                'db_table': 'livros_view',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='autor',
            table='autores',
        ),
        migrations.AlterModelTable(
            name='editora',
            table='editoras',
        ),
        migrations.AlterModelTable(
            name='genero',
            table='generos',
        ),
        migrations.AlterModelTable(
            name='livro',
            table='livros',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]

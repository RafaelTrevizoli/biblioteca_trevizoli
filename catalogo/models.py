# models.py
from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)

    class Meta:
        db_table = 'autores'

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'editoras'

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'generos'

    def __str__(self):
        return self.nome

class Tag(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True, blank=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        db_table = 'livros'

    def __str__(self):
        return self.titulo

class LivroView(models.Model):
    id = models.IntegerField(primary_key=True)
    livro_titulo = models.CharField(max_length=255)
    autor_nome = models.CharField(max_length=255)
    editora_nome = models.CharField(max_length=255)
    genero_nome = models.CharField(max_length=255)
    tags_nomes = models.TextField()

    class Meta:
        managed = False
        db_table = 'livros_view'

    def __str__(self):
        return self.livro_titulo

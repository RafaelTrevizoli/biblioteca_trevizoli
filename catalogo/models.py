from django.db import models
from django.contrib.auth.models import User

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

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'emprestimos'

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo}"

class Log(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data = models.DateTimeField()

    class Meta:
        db_table = 'logs'

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo} "

class EmprestimoUsuarioView(models.Model):
    usuario = models.CharField(max_length=150, primary_key=True)
    livro = models.CharField(max_length=200)
    data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'emprestimos_usuario'
        verbose_name = "Empréstimo por Usuário"
        verbose_name_plural = "Empréstimos por Usuário"

    def __str__(self):
        return f"{self.usuario} - {self.livro}"

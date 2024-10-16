# forms.py
from django import forms
from .models import Livro, Autor, Editora, Genero

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'ano_publicacao', 'autor', 'editora', 'genero']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'biografia']

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'endereco']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nome']

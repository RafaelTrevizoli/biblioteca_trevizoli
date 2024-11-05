from django import forms
from .models import Livro, Autor, Editora, Genero, Tag

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'descricao', 'ano_publicacao', 'autor', 'editora', 'genero', 'tags']

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

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Livro, Autor, Editora, Genero, Tag
from .forms import LivroForm, AutorForm, EditoraForm, GeneroForm, TagForm


# --- Livros --- #
def listar_livros(request):
    query = request.GET.get('buscar')
    if query:
        livros = Livro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__nome__icontains=query) |
            Q(editora__nome__icontains=query) |
            Q(genero__nome__icontains=query) |
            Q(tags__nome__icontains=query)
        ).distinct()
    else:
        livros = Livro.objects.all()

    return render(request, 'catalogo/livros/listar_livros.html', {'livros': livros})


def listar_livros_crud(request):
    livros = Livro.objects.all()
    return render(request, 'catalogo/livros/listar_livros_crud.html', {'livros': livros})


def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros_crud')
    else:
        form = LivroForm()

    return render(request, 'catalogo/livros/criar_livro.html', {'form': form})


def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros_crud')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'catalogo/livros/editar_livro.html', {'form': form})


def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros_crud')
    return render(request, 'catalogo/livros/deletar_livro.html', {'livro': livro})


def detalhes_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'catalogo/livros/detalhes_livro.html', {'livro': livro})


# --- Autores --- #
def listar_autores(request):
    query = request.GET.get('buscar')
    if query:
        autores = Autor.objects.filter(
            Q(nome__icontains=query) |
            Q(biografia__icontains=query)
        ).distinct()
    else:
        autores = Autor.objects.all()

    return render(request, 'catalogo/autores/listar_autores.html', {'autores': autores})


def listar_autores_crud(request):
    autores = Autor.objects.all()
    return render(request, 'catalogo/autores/listar_autores_crud.html', {'autores': autores})


def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores_crud')
    else:
        form = AutorForm()
    return render(request, 'catalogo/autores/criar_autor.html', {'form': form})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores_crud')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/autores/editar_autor.html', {'form': form})


def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores_crud')
    return render(request, 'catalogo/autores/deletar_autor.html', {'autor': autor})


def detalhes_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'catalogo/autores/detalhes_autor.html', {'autor': autor})


# --- Editoras --- #

def listar_editoras_crud(request):
    editoras = Editora.objects.all()
    return render(request, 'catalogo/editoras/listar_editoras_crud.html', {'editoras': editoras})


def criar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_editoras_crud')
    else:
        form = EditoraForm()
    return render(request, 'catalogo/editoras/criar_editora.html', {'form': form})


def editar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('listar_editoras_crud')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'catalogo/editoras/editar_editora.html', {'form': form})


def deletar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        return redirect('listar_editoras_crud')
    return render(request, 'catalogo/editoras/deletar_editora.html', {'editora': editora})


def detalhes_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    return render(request, 'catalogo/editoras/detalhes_editora.html', {'editora': editora})


# --- Gêneros --- #

def listar_generos_crud(request):
    generos = Genero.objects.all()
    return render(request, 'catalogo/generos/listar_generos_crud.html', {'generos': generos})


def criar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_generos_crud')
    else:
        form = GeneroForm()
    return render(request, 'catalogo/generos/criar_genero.html', {'form': form})


def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('listar_generos_crud')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'catalogo/generos/editar_genero.html', {'form': form})


def deletar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('listar_generos_crud')
    return render(request, 'catalogo/generos/deletar_genero.html', {'genero': genero})


def detalhes_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    return render(request, 'catalogo/generos/detalhes_genero.html', {'genero': genero})


# --- Tags --- #

def listar_tags_crud(request):
    tags = Tag.objects.all()
    return render(request, 'catalogo/tags/listar_tags_crud.html', {'tags': tags})


def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tags_crud')
    else:
        form = TagForm()
    return render(request, 'catalogo/tags/criar_tag.html', {'form': form})


def editar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('listar_tags_crud')
    else:
        form = TagForm(instance=tag)
    return render(request, 'catalogo/tags/editar_tag.html', {'form': form})


def deletar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('listar_tags_crud')
    return render(request, 'catalogo/tags/deletar_tag.html', {'tag': tag})


def detalhes_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'catalogo/tags/detalhes_tag.html', {'tag': tag})

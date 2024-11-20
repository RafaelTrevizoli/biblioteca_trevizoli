from .models import Livro, Autor, Editora, Genero, Tag, Emprestimo, Log
from .forms import LivroForm, AutorForm, EditoraForm, GeneroForm, TagForm
from django.db.models import Q
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.core.paginator import Paginator


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

    # --- Paginator --- #
    paginator = Paginator(livros, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Obter os top 3 livros mais emprestados
    top_livros = get_top_3_livros()

    # Passando os dados para o template
    return render(request, 'catalogo/livros/listar_livros.html', {
        'page_obj': page_obj,
        'top_livros': top_livros
    })


@permission_required('', login_url='pagina_de_erro')
def listar_livros_crud(request):
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

    # --- Paginator --- #
    paginator = Paginator(livros, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/livros/listar_livros_crud.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro adicionado com sucesso!')
            return redirect('listar_livros_crud')
    else:
        form = LivroForm()

    return render(request, 'catalogo/livros/criar_livro.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro editado com sucesso!')
            return redirect('listar_livros_crud')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'catalogo/livros/editar_livro.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
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

    # --- Paginator --- #
    paginator = Paginator(autores, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/autores/listar_autores.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def listar_autores_crud(request):
    query = request.GET.get('buscar')

    if query:
        autores = Autor.objects.filter(
            Q(nome__icontains=query) |
            Q(biografia__icontains=query)
        ).distinct()
    else:
        autores = Autor.objects.all()

    # --- Paginator --- #
    paginator = Paginator(autores, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/autores/listar_autores_crud.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor adicionado com sucesso!')
            return redirect('listar_autores_crud')
    else:
        form = AutorForm()
    return render(request, 'catalogo/autores/criar_autor.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor editado com sucesso!')
            return redirect('listar_autores_crud')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'catalogo/autores/editar_autor.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor deletado com sucesso!')
        return redirect('listar_autores_crud')
    return render(request, 'catalogo/autores/deletar_autor.html', {'autor': autor})


def detalhes_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'catalogo/autores/detalhes_autor.html', {'autor': autor})


# --- Editoras --- #

@permission_required('', login_url='pagina_de_erro')
def listar_editoras_crud(request):
    query = request.GET.get('buscar')

    if query:
        editoras = Editora.objects.filter(
            Q(nome__icontains=query) |
            Q(endereco__icontains=query)
        ).distinct()
    else:
        editoras = Editora.objects.all()

    paginator = Paginator(editoras, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/editoras/listar_editoras_crud.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def criar_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora adicionada com sucesso!')
            return redirect('listar_editoras_crud')
    else:
        form = EditoraForm()
    return render(request, 'catalogo/editoras/criar_editora.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def editar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora editada com sucesso!')
            return redirect('listar_editoras_crud')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'catalogo/editoras/editar_editora.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def deletar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        messages.success(request, 'Editora deletada com sucesso!')
        return redirect('listar_editoras_crud')
    return render(request, 'catalogo/editoras/deletar_editora.html', {'editora': editora})


@permission_required('', login_url='pagina_de_erro')
def detalhes_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    return render(request, 'catalogo/editoras/detalhes_editora.html', {'editora': editora})


# --- Gêneros --- #

@permission_required('', login_url='pagina_de_erro')
def listar_generos_crud(request):
    query = request.GET.get('buscar')

    if query:
        generos = Genero.objects.filter(
            Q(nome__icontains=query)
        ).distinct()
    else:
        generos = Genero.objects.all()

    paginator = Paginator(generos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/generos/listar_generos_crud.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def criar_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gênero adicionado com sucesso!')
            return redirect('listar_generos_crud')
    else:
        form = GeneroForm()
    return render(request, 'catalogo/generos/criar_genero.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def editar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        form = GeneroForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gênero editado com sucesso!')
            return redirect('listar_generos_crud')
    else:
        form = GeneroForm(instance=genero)
    return render(request, 'catalogo/generos/editar_genero.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def deletar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        messages.success(request, 'Gênero deletado com sucesso!')
        return redirect('listar_generos_crud')
    return render(request, 'catalogo/generos/deletar_genero.html', {'genero': genero})


@permission_required('', login_url='pagina_de_erro')
def detalhes_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    return render(request, 'catalogo/generos/detalhes_genero.html', {'genero': genero})


# --- Tags --- #

@permission_required('', login_url='pagina_de_erro')
def listar_tags_crud(request):
    query = request.GET.get('buscar')

    if query:
        tags = Tag.objects.filter(
            Q(nome__icontains=query)
        ).distinct()
    else:
        tags = Tag.objects.all()

    paginator = Paginator(tags, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalogo/tags/listar_tags_crud.html', {'page_obj': page_obj})


@permission_required('', login_url='pagina_de_erro')
def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag adicionada com sucesso!')
            return redirect('listar_tags_crud')
    else:
        form = TagForm()
    return render(request, 'catalogo/tags/criar_tag.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def editar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tag editada com sucesso!')
            return redirect('listar_tags_crud')
    else:
        form = TagForm(instance=tag)
    return render(request, 'catalogo/tags/editar_tag.html', {'form': form})


@permission_required('', login_url='pagina_de_erro')
def deletar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, 'Tag deletada com sucesso!')
        return redirect('listar_tags_crud')
    return render(request, 'catalogo/tags/deletar_tag.html', {'tag': tag})


@permission_required('', login_url='pagina_de_erro')
def detalhes_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'catalogo/tags/detalhes_tag.html', {'tag': tag})


# --- User --- #

@login_required
def informacoes_usuario(request):
    user = request.user
    return render(request, 'contas/informacoes_usuario.html', {'user': user})


# --- Página de erro --- #
def pagina_de_erro(request):
    return render(request, 'reusable/pag_erro.html')


# --- Emprestimos --- #
def meus_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, 'catalogo/emprestimo/meus_emprestimos.html', {'emprestimos': emprestimos})


def visualizar_livro_emprestimos(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    emprestimo = Emprestimo.objects.filter(usuario=request.user, livro=livro).first()

    if emprestimo:
        return render(request, 'catalogo/emprestimo/visualizar_livro.html', {'livro': livro})
    else:
        return render(request, '', {'mensagem': 'Você não tem acesso a este livro.'})


@login_required
def obter_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if not Emprestimo.objects.filter(usuario=request.user, livro=livro).exists():
        Emprestimo.objects.create(usuario=request.user, livro=livro)

        messages.info(request, 'Livro adicionado a sua conta!')

        return redirect(request.META.get('HTTP_REFERER'))

    else:
        messages.error(request, 'Este livro já foi adicionado a sua conta!')

        return redirect(request.META.get('HTTP_REFERER'))  # --- Redireciona de volta para a página anterior --- #


# --- Chicão --- #

# --- Trigger para o admin vizualizar os livros "emprestados" aos usuários --- #

from django.db.models import Q


def logs_view(request):
    query = request.GET.get('q')
    order = request.GET.get('order', 'recent')

    logs = Log.objects.all()

    # Filtrando logs por nome de usuário
    if query:
        logs = logs.filter(Q(usuario__username__icontains=query))

    # Ordenando logs por data
    if order == 'recent':
        logs = logs.order_by('-data')  # Mais recente
    else:
        logs = logs.order_by('data')  # Mais antigo

    return render(request, 'catalogo/emprestimo/emprestimos_log.html', {
        'logs': logs,
        'query': query,
        'order': order,
    })


# --- Procidure para listar os top 3 livros mais obtidos --- #

def get_top_3_livros():
    with connection.cursor() as cursor:
        cursor.callproc('top_3_livros_mais_emprestados')
        result = cursor.fetchall()
        return result

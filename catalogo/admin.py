from django.contrib import admin
from .models import Autor, Livro, Editora, Genero,Tag, EmprestimoUsuarioView


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')
    search_fields = ('nome',)

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'editora', 'genero', 'ano_publicacao')
    list_filter = ('autor', 'editora', 'genero')
    search_fields = ('titulo',)


@admin.register(EmprestimoUsuarioView)
class EmprestimoUsuarioViewAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'data')
    ordering = ('usuario', 'livro', 'data')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
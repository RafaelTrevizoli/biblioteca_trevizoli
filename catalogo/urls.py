# urls.py
from django.urls import path
from . import views

urlpatterns = [

    # --- Livros ---
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/tela/', views.listar_livros_crud, name='listar_livros_crud'),
    path('livros/<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('livros/criar/', views.criar_livro, name='criar_livro'),
    path('livros/editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('livros/deletar/<int:pk>/', views.deletar_livro, name='deletar_livro'),

    # --- Autores ---
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/tela/', views.listar_autores_crud, name='listar_autores_crud'),
    path('autores/criar/', views.criar_autor, name='criar_autor'),
    path('autores/<int:pk>/', views.detalhes_autor, name='detalhes_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/deletar/<int:pk>/', views.deletar_autor, name='deletar_autor'),

    # --- Editoras ---

    path('editoras/tela/', views.listar_editoras_crud, name='listar_editoras_crud'),
    path('editoras/criar/', views.criar_editora, name='criar_editora'),
    path('editoras/<int:pk>/', views.detalhes_editora, name='detalhes_editora'),
    path('editoras/editar/<int:pk>/', views.editar_editora, name='editar_editora'),
    path('editoras/deletar/<int:pk>/', views.deletar_editora, name='deletar_editora'),

    # --- Gêneros ---

    path('generos/tela/', views.listar_generos_crud, name='listar_generos_crud'),
    path('generos/criar/', views.criar_genero, name='criar_genero'),
    path('generos/<int:pk>/', views.detalhes_genero, name='detalhes_genero'),
    path('generos/editar/<int:pk>/', views.editar_genero, name='editar_genero'),
    path('generos/deletar/<int:pk>/', views.deletar_genero, name='deletar_genero'),
]

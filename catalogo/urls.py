from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [

    # --- Admin --- #
    path('admin/', admin.site.urls),

    # --- Página de erro --- #

    path('pagina_de_erro/', views.pagina_de_erro, name='pagina_de_erro'),

    # --- Pasta Raiz --- #
    path('', views.listar_livros, name='listar_livros'),

    # --- Chicão --- #

    # --- Trigger para o admin vizualizar os livros "emprestados" aos usuários --- #
    path('logs/', views.logs_view, name='logs'),  # Adiciona a URL para exibir os logs

    # --- Emprestimos --- #

    path('meus-emprestimos/', views.meus_emprestimos, name='meus_emprestimos'),
    path('livro/<int:livro_id>/', views.visualizar_livro_emprestimos, name='visualizar_livro_emprestimos'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('livro/<int:livro_id>/obter/', views.obter_livro, name='obter_livro'),

    # --- Livros --- #
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/tela/', views.listar_livros_crud, name='listar_livros_crud'),
    path('livros/<int:pk>/', views.detalhes_livro, name='detalhes_livro'),
    path('livros/criar/', views.criar_livro, name='criar_livro'),
    path('livros/editar/<int:pk>/', views.editar_livro, name='editar_livro'),
    path('livros/deletar/<int:pk>/', views.deletar_livro, name='deletar_livro'),

    # --- Autores --- #
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/tela/', views.listar_autores_crud, name='listar_autores_crud'),
    path('autores/criar/', views.criar_autor, name='criar_autor'),
    path('autores/<int:pk>/', views.detalhes_autor, name='detalhes_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/deletar/<int:pk>/', views.deletar_autor, name='deletar_autor'),

    # --- Editoras --- #

    path('editoras/tela/', views.listar_editoras_crud, name='listar_editoras_crud'),
    path('editoras/criar/', views.criar_editora, name='criar_editora'),
    path('editoras/<int:pk>/', views.detalhes_editora, name='detalhes_editora'),
    path('editoras/editar/<int:pk>/', views.editar_editora, name='editar_editora'),
    path('editoras/deletar/<int:pk>/', views.deletar_editora, name='deletar_editora'),

    # --- Generos --- #

    path('generos/tela/', views.listar_generos_crud, name='listar_generos_crud'),
    path('generos/criar/', views.criar_genero, name='criar_genero'),
    path('generos/<int:pk>/', views.detalhes_genero, name='detalhes_genero'),
    path('generos/editar/<int:pk>/', views.editar_genero, name='editar_genero'),
    path('generos/deletar/<int:pk>/', views.deletar_genero, name='deletar_genero'),

    # --- Tags --- #
    path('tags/', views.listar_tags_crud, name='listar_tags_crud'),
    path('tags/criar/', views.criar_tag, name='criar_tag'),
    path('tags/editar/<int:pk>/', views.editar_tag, name='editar_tag'),
    path('tags/deletar/<int:pk>/', views.deletar_tag, name='deletar_tag'),
    path('tags/<int:pk>/', views.detalhes_tag, name='detalhes_tag'),

]


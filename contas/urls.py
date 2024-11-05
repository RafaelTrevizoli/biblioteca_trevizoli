from django.urls import path
from .views import RegisterView, login_view, logout_view, informacoes_usuario, verifica_usuario

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('informacoes_usuario/', informacoes_usuario, name='informacoes_usuario'),
    path('verifica_usuario/', verifica_usuario, name='verifica_usuario'),
]

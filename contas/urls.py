from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('informacoes_usuario/', views.informacoes_usuario, name='informacoes_usuario'),
    path('verifica_usuario/', views.verifica_usuario, name='verifica_usuario'),
]

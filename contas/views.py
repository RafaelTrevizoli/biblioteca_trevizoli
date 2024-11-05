from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# --- Registro --- #
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'contas/register.html'
    success_url = reverse_lazy('login')

# --- Login --- #
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_livros')
    return render(request, 'contas/login.html')

# --- Logout --- #
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def informacoes_usuario(request):
    user = request.user
    return render(request, 'contas/informacoes_usuario.html', {'user': user})

def verifica_usuario(request):
    if request.user.is_authenticated:
        return redirect('informacoes_usuario')
    else:
        return redirect('login')
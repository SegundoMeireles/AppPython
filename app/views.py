from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
#Página inicial
def home(request):
    return render(request,'home.html')

#Form de cadastro de usuários
def create(request):
    return render(request,'create.html')

#Inserção dos dados do usuário no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senhas diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'

    return render(request,'create.html', data)

#Formulário do painel de Login
def painel(request):
    return render(request,'painel.html')

#Processa o Login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválida!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html', data)

#Página inicial do dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Página de questionário
def questionario(request):
    return render(request,'dashboard/questionario.html')
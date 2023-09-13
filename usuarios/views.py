from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
  form = LoginForms()

  # criar o if dizendo que, se o método for POST, teremos outro retorno que não a renderização da página com o formulário em branco
  if request.method == "POST":
    # As lógicas de login e de cadastro são sempre baseadas em validações!
    form = LoginForms(request.POST)

    # Agora, precisamos conferir se o formulário está válido:
    if form.is_valid():
      
      # Buscaremos as informações inseridas no form de login que irão ser validadas:
      nome = form["nome_login"].value()
      senha = form["senha"].value()

      # O Django facilita esse processo com um método próprio para isso: o auth. Vamos importá-lo: from django.contrib import auth
      usuario = auth.authenticate(
        request,
        username=nome,
        password=senha
      ) # Essa variável será retornada como válida, que não pode ser retornada como "none"
      if usuario is not None:
        auth.login(request, usuario)
        messages.success(request, "Login efetuado com sucesso!")
        return redirect('index')
      else:
        messages.error(request, "Erro ao efetuar login")
        return redirect('login')

  return render(request, "usuarios/login.html", {"form" : form})

def cadastro(request):
  form = CadastroForms()

  if request.method == "POST":
    form = CadastroForms(request.POST)

    if form.is_valid():  # Retorna True se o form for válido e False se não for

      # Verificando se as senhas são iguais e se não for redireciona para o cadastro novamente.
      if form["senha_1"].value() != form["senha_2"].value():
        messages.error(request, 'Senhas não são iguais')
        return redirect('cadastro')

      # Criando variáveis com as infos que pegamos nos inputs para que possamos usá-las no cadastro de um novo usuário dentro da base de dados;
      nome = form["nome_cadastro"].value()
      email = form["email"].value()
      senha = form["senha_1"].value()

      # Antes de fazer o cadastro do usuário dentro da base de dados, temos que verificar se ele já existe dentro da mesma. Para isso, faremos o seguinte:
      # Para acessar o usuário, importaremos a tabela de usuários que fica dentro do Django --> from django.contrib.auth.models import User
      # Agora faremos um if:
      if User.objects.filter(username=nome).exists():
        messages.error(request, 'Usuário já existente')
        return redirect("cadastro")
      
      usuario = User.objects.create_user(
        username=nome,
        email=email,
        password=senha
      )
      usuario.save()
      messages.success(request, 'Cadastro efetuado com sucesso!')
      return redirect('login')

  return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
  auth.logout(request)
  messages.success(request, "Logout efetuado com sucesso!")
  return redirect("login")
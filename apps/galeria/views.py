from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

# Create your views here.
# Aqui que você irá mostrar as páginas do seu app. Nelas você irá fazer a conexão com os arquivos html vindo de templates.


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect("login")

    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(
        request,
        "galeria/index.html",
        { "cards" : fotografia } # Aqui você envia para o arquivo os dados via model que criamos;
    )  # Essa propriedade render é a responsável por pegar os arquivos do template, a partir de uma requisição http vinda do urls.py, e mostrar para o usuário.
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) 
    return render(
        request,
        "galeria/imagem.html",
        {"fotografia" : fotografia}
    )

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect("login")

    fotografia = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar: 
            fotografia = fotografia.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografia})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect("login")
    
    form = FotografiaForms()
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():  # Retorna True se o form for válido e False se não for
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, "galeria/nova_imagem.html", {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass

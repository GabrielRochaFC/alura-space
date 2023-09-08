from django.shortcuts import render

# Create your views here.
# Aqui que você irá mostrar as páginas do seu app. Nelas você irá fazer a conexão com os arquivos html vindo de templates.


def index(request):
    return render(
        request, "galeria/index.html"
    )  # Essa propriedade render é a responsável por pegar os arquivos do template, a partir de uma requisição http vinda do urls.py, e mostrar para o usuário.
def imagem(request):
    return render(
        request, "galeria/imagem.html"
    )

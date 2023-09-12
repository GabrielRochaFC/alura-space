from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Create your views here.
# Aqui que você irá mostrar as páginas do seu app. Nelas você irá fazer a conexão com os arquivos html vindo de templates.


def index(request):
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

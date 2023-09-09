# Aqui ficarão os urls somente do App galeria. Dessa forma ficará mais organizado.

from django.urls import path
from galeria.views import index, imagem

# Lista com todos os endereços da galeria
urlpatterns = [
  path("", index, name = 'index'),
  path("imagem/", imagem, name = 'imagem')
]

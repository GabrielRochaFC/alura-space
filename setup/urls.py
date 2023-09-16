"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# É aqui que você consegue colocar todas as rotas do seu projeto. Ele que controla tudo isso dentro do Django. Mas o ideal não é colocar tudo numa unica parte. Por isso deve-se dividir usando o 'include' e selecionando o caminho onde vai ficar o Urls de cada projeto. Dessa forma fica mais organizado.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.galeria.urls")),
    path("", include("apps.usuarios.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

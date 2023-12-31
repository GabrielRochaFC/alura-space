from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
  list_display = ("id", "nome", "legenda", "publicada",)
  list_display_links = ("id", "nome")
  search_fields = ("nome",)
  list_filter = ("categoria", "usuario",)
  list_per_page = 5
  list_editable = ("publicada",)

# Register your models here.

admin.site.register(Fotografia, ListandoFotografias)

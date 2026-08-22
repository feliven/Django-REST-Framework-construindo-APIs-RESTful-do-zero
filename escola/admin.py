from django.contrib import admin
from escola.models import Estudante, Curso


# Register your models here.
class ListandoEstudantes(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_editable = ("email",)
    list_per_page = 10


class ListandoCursos(admin.ModelAdmin):
    list_display = ("codigo", "descricao", "nivel")
    list_display_links = ("codigo",)
    search_fields = ("codigo", "descricao")
    list_filter = ("nivel",)
    list_editable = ("nivel",)
    list_per_page = 10


admin.site.register(Estudante, ListandoEstudantes)
admin.site.register(Curso, ListandoCursos)

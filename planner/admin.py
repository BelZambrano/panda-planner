from django.contrib import admin
from .models import Meta


@admin.register(Meta)
class MetaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "completada", "fecha_creacion")
    list_filter = ("completada", "fecha_creacion")
    search_fields = ("titulo", "descripcion")

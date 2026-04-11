from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("habitos/", views.habitos, name="habitos"),
    path("metas/", views.metas, name="metas"),
    path("metas/nueva/", views.nueva_meta, name="nueva_meta"),
    path("metas/editar/<int:meta_id>/", views.editar_meta, name="editar_meta"),
    path("metas/eliminar/<int:meta_id>/", views.eliminar_meta, name="eliminar_meta"),
    path("sobre/", views.sobre, name="sobre"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("metas/", views.metas, name="metas"),
    path("metas/nueva/", views.nueva_meta, name="nueva_meta"),
    path("metas/editar/<int:meta_id>/", views.editar_meta, name="editar_meta"),
    path("metas/eliminar/<int:meta_id>/", views.eliminar_meta, name="eliminar_meta"),
    path("metas/toggle/<int:meta_id>/", views.toggle_meta, name="toggle_meta"),
    path("habitos/", views.habitos, name="habitos"),
    path("habitos/nuevo/", views.nuevo_habito, name="nuevo_habito"),
    path("habitos/editar/<int:habito_id>/", views.editar_habito, name="editar_habito"),
    path(
        "habitos/eliminar/<int:habito_id>/",
        views.eliminar_habito,
        name="eliminar_habito",
    ),
    path("habitos/toggle/<int:habito_id>/", views.toggle_habito, name="toggle_habito"),
]

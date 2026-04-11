from django.shortcuts import render, redirect, get_object_or_404
from .models import Meta
from .forms import MetaForm


def home(request):
    return render(request, "home.html")


def habitos(request):
    return render(request, "habitos.html")


def metas(request):
    metas = Meta.objects.all().order_by("-fecha_creacion")
    return render(request, "metas.html", {"metas": metas})


def nueva_meta(request):
    if request.method == "POST":
        form = MetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("metas")
    else:
        form = MetaForm()

    return render(request, "nueva_meta.html", {"form": form})


def editar_meta(request, meta_id):
    meta = get_object_or_404(Meta, id=meta_id)

    if request.method == "POST":
        form = MetaForm(request.POST, instance=meta)
        if form.is_valid():
            form.save()
            return redirect("metas")
    else:
        form = MetaForm(instance=meta)

    return render(request, "editar_meta.html", {"form": form, "meta": meta})


def eliminar_meta(request, meta_id):
    meta = get_object_or_404(Meta, id=meta_id)

    if request.method == "POST":
        meta.delete()
        return redirect("metas")

    return render(request, "eliminar_meta.html", {"meta": meta})


def sobre(request):
    return render(request, "sobre.html")

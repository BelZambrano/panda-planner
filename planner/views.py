from django.shortcuts import render, redirect, get_object_or_404
from .models import Meta, Habito
from .forms import MetaForm, HabitoForm


def home(request):
    return render(request, "home.html")


def sobre(request):
    return render(request, "sobre.html")


# --------------------
# METAS
# --------------------


def metas(request):
    metas = Meta.objects.all().order_by("completada", "-fecha_creacion")
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

    return redirect("metas")


def toggle_meta(request, meta_id):
    meta = get_object_or_404(Meta, id=meta_id)
    meta.completada = not meta.completada
    meta.save()
    return redirect("metas")


# --------------------
# HÁBITOS
# --------------------


def habitos(request):
    habitos = Habito.objects.all().order_by("completado", "-fecha_creacion")
    return render(request, "habitos.html", {"habitos": habitos})


def nuevo_habito(request):
    if request.method == "POST":
        form = HabitoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("habitos")
    else:
        form = HabitoForm()

    return render(request, "nueva_habito.html", {"form": form})


def editar_habito(request, habito_id):
    habito = get_object_or_404(Habito, id=habito_id)

    if request.method == "POST":
        form = HabitoForm(request.POST, instance=habito)
        if form.is_valid():
            form.save()
            return redirect("habitos")
    else:
        form = HabitoForm(instance=habito)

    return render(request, "editar_habito.html", {"form": form, "habito": habito})


def eliminar_habito(request, habito_id):
    habito = get_object_or_404(Habito, id=habito_id)

    if request.method == "POST":
        habito.delete()
        return redirect("habitos")

    return redirect("habitos")


def toggle_habito(request, habito_id):
    habito = get_object_or_404(Habito, id=habito_id)
    habito.completado = not habito.completado
    habito.save()
    return redirect("habitos")

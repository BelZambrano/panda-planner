from django.shortcuts import render, redirect, get_object_or_404
from .models import Meta, Habito
from .forms import MetaForm, HabitoForm


def home(request):
    metas_pendientes = Meta.objects.filter(completada=False).count()
    metas_completadas = Meta.objects.filter(completada=True).count()
    habitos_activos = Habito.objects.filter(completado=False).count()

    context = {
        "metas_pendientes": metas_pendientes,
        "metas_completadas": metas_completadas,
        "habitos_activos": habitos_activos,
    }

    return render(request, "home.html", context)


def sobre(request):
    return render(request, "sobre.html")


# --------------------
# METAS
# --------------------


def metas(request):
    estado = request.GET.get("estado", "todas")

    metas = Meta.objects.all()

    if estado == "pendientes":
        metas = metas.filter(completada=False).order_by("-fecha_creacion")
    elif estado == "completadas":
        metas = metas.filter(completada=True).order_by(
            "-fecha_completada", "-fecha_creacion"
        )
    else:
        metas = metas.order_by("completada", "-fecha_creacion")

    context = {
        "metas": metas,
        "estado_actual": estado,
    }

    return render(request, "metas.html", context)


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
    estado = request.GET.get("estado", "todos")

    habitos = Habito.objects.all()

    if estado == "activos":
        habitos = habitos.filter(completado=False).order_by("-fecha_creacion")
    elif estado == "completados":
        habitos = habitos.filter(completado=True).order_by("-fecha_creacion")
    else:
        habitos = habitos.order_by("completado", "-fecha_creacion")

    context = {
        "habitos": habitos,
        "estado_actual": estado,
    }

    return render(request, "habitos.html", context)


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

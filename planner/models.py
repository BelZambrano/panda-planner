from django.db import models
from django.utils import timezone


class Meta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.completada and not self.fecha_completada:
            self.fecha_completada = timezone.now()
        elif not self.completada:
            self.fecha_completada = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Habito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

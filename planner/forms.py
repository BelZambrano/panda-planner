from django import forms
from .models import Meta, Habito


class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ["titulo", "descripcion", "completada"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Ej: Terminar Panda Planner",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-textarea",
                    "placeholder": "Describe tu meta...",
                    "rows": 4,
                }
            ),
            "completada": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }


class HabitoForm(forms.ModelForm):
    class Meta:
        model = Habito
        fields = ["nombre", "descripcion", "completado"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Ej: Tomar agua"}
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-textarea",
                    "placeholder": "Describe tu hábito...",
                    "rows": 4,
                }
            ),
            "completado": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }

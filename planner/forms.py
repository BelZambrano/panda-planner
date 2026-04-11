from django import forms
from .models import Meta


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

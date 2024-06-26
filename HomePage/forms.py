from django import forms
from .models import Produtos, PerfilUsuario
from django.core.validators import MinValueValidator

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'description', 'tags', 'valor', 'imagem', 'quantidade']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'min': '1', 'type': 'number'}),
        }
    quantidade = forms.IntegerField(validators=[MinValueValidator(1)])
        
    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")
        return valor

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['imagem_perfil']
        
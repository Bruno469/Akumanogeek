from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'description', 'tags', 'valor', 'imagem']
        
    def clean_valor(self):
        valor = self.cleaned_data['valor']
        if valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")
        return valor
from typing import Any
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. I1nform a valid email address')
    nome = forms.CharField(min_length=3, max_length=32)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmação da senha', widget=forms.PasswordInput)
    phone_number = PhoneNumberField(label='Telefone', min_length=10, max_length=15)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem. Por favor, tente novamente.")

        return cleaned_data


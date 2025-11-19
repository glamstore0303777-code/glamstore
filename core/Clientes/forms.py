# core/Clientes/forms.py
from django import forms

class LoginForm(forms.Form):
    usuario = forms.EmailField(label='Correo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
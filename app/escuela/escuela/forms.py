# escuela/forms.py
from django import forms
from django.contrib.auth.models import User


class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico', max_length=100)  # Agregamos el campo email
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre completo', max_length=100)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')  # Agregamos el campo email a los campos del formulario


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']  # Asignamos el correo electrónico al usuario
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


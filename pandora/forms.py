from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class UserEditForm(UserChangeForm):

  password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
  )

  password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
  password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name')

  def clean_password2(self):
    
    print(self.cleaned_data)

    password1 = self.cleaned_data["password1"]
    password2 = self.cleaned_data["password2"]

    if password2 != password1:
      raise forms.ValidationError("Las contraseñas no son iguales")
    
    else:
      return password2
    

class AvatarFormulario(forms.ModelForm):

  class Meta:
    model=Avatar
    fields=('imagen',)

  def clean_imagen(self):
    imagen = self.cleaned_data.get('imagen')
    if not imagen:
      raise forms.ValidationError("Debes seleccionar una imagen.")
    return imagen

class ConfirmarEliminacionForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirmo que quiero eliminar mi avatar.")

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15, required=False)
    mensaje = forms.CharField(widget=forms.Textarea)
from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese el usuario'}), max_length=15, label='Usuario'
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese la contraseña'}), label='Contraseña',  max_length=10,
    )
    not_expire = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control'}), required=False,
                                    label='No caduca la sesión')
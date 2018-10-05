from django import forms


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}),max_length=30, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',}), label='Contraseña')
    not_expire = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-control',}),required=False,
                                    label='No caduca la sesión')
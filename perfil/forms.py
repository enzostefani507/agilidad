from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from perfil.models import Usuario

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({'class' : 'form-control','placeholder' : "Correo electronico", 'type' : 'text','autofocus': 'autofocus'})
        self.fields["password"].widget.attrs.update({'class' : 'form-control','placeholder' : "Contraseña", 'type' : 'text'})

class SignInForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder':'Nombre de usuario',
                'autofocus':True
            }
        )
        self.fields["foto"].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder' : "URL de su foto",
                'type' : 'text',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder':"Correo electronico"
            }
        )
        self.fields["password1"].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder' : "Contraseña",
                'type' : 'text',
            }
        )
        self.fields["password2"].widget.attrs.update(
            {
                'class' : 'form-control',
                'placeholder' : "Repita su contraseña",
                'type' : 'text',
            }
        )
        

    email = forms.EmailField(required=True)
    foto = forms.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ("username","foto","email", "password1", "password2",)

    
    def save(self, commit=True):
        user = super(SignInForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        if user.is_active:
            print('esta activado')
        return user
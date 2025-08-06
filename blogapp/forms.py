from django import forms
from blogapp.models import Post,Registation


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registation
        fields = ['username', 'password', 'email', 'phone']
        widgets = {
            'password': forms.PasswordInput(),
        }
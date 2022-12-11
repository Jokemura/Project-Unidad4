from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectRegister
#creamos clase para crear usuarios 
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        
        model = User
        
        fields = ("username", "first_name", "last_name", "email",  "password1", "password2")

    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class InputProject(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.TextInput()
    url = forms.URLField(max_length=30)
    image = forms.ImageField(allow_empty_file=True)
    tags= forms.CharField(max_length=10) 
    

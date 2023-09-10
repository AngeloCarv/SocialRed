from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='your password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm your password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }
        
class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,'placeholder':'Post Now !'}),required=True)
     
    class Meta:
        model = Post
        fields = ['content']
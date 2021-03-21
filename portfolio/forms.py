from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, User

class UserProfileForm(forms.ModelForm):
    
    class Meta():
        model = UserProfile
        fields = ['title', 'about', 'img', 'github', 'linkedin']
        
        
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ['email', 'username', 'password']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    

from django import forms

from .models import ContactModel

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ['email', 'title', 'text']
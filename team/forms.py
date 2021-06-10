from django import forms
from django.core.exceptions import ValidationError

from .models import OurTeam

class TeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = '__all__'
        
    def clean_user(self):
        data = self.cleaned_data.get('user')
        if data.is_staff:
            return data
        else:
            raise ValidationError('User must be staff')
        
from django import forms
from .models import Dashboard

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ('resume', 'email', 'phone')    

        widgets = {
            'resume': forms.FileInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
        }
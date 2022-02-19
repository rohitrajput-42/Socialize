from django import forms
from .models import Dashboard, Job

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ('resume', 'email', 'phone')    

        widgets = {
            'resume': forms.FileInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control col-sm-5 ml-5'}),
        }

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('company_name', 'job_title', 
                  'company_logo', 'experience',
                  'company_description', 'job_details', 'location',
                  'recruiter', 'contact', 'payrate', 'skills_tag',
                  'job_status', 'apply_by', 'Duration')
        
        widgets = {
            'apply_by' : forms.DateInput(attrs = {'type': 'Date'}),
            'Duration': forms.NumberInput(attrs = {'placeholder': 'In yrs.'}),
            'recruiter': forms.TextInput(attrs = {'placeholder': 'Contact info of the recruiter'}),
            'experience': forms.NumberInput(attrs = {'placeholder': 'In yrs.'}),
        }
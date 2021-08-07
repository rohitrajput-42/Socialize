import django_filters
from django_filters import DateFilter
from .models import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['company_name', 'job_title',  'education', 
                   'company_logo', 'experience', 'industry',
                   'company_description', 'job_details', 'location', 
                   'recruiter', 'contact', 'payrate', 'updated', 'created', 
                   'skills_tag', 'apply_by', 'Duration']

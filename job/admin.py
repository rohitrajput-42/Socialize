from django.contrib import admin
from .models import Job, Dashboard

class AdminJob(admin.ModelAdmin):
    list_display = ['company_name', 'industry', 'skills_tag', 'location', 'contact', 'created']

class AdminDashboard(admin.ModelAdmin):
    list_display = ['job', 'user', 'email', 'phone', 'job_status', 'date_applied']

admin.site.register(Job, AdminJob)
admin.site.register(Dashboard, AdminDashboard)
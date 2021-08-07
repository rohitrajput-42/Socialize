from django.urls import path
from .views import Jobpage, JobDetailView, Jobdashboard

urlpatterns = [
    path('', Jobpage, name = "job_page"),
    path('job/<int:id>', JobDetailView, name = "job_detail"),
    path('dashboard', Jobdashboard, name = "dashboard")
] 
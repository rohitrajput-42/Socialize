from django.urls import path
from .views import Jobpage, JobDetailView, Jobdashboard,Post_job

urlpatterns = [
    path('', Jobpage, name = "job_page"),
    path('job/<int:id>', JobDetailView, name = "job_detail"),
    path('dashboard', Jobdashboard, name = "dashboard"),
    path('post_job', Post_job, name = "post_job")
] 
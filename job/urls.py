from django.urls import path
from .views import *

urlpatterns = [
    path('', Jobpage, name = "job_page"),
    path('job/<int:id>/', JobDetailView, name = "job_detail"),
    path('dashboard/', Jobdashboard, name = "dashboard"),
    path('detail_dash/<int:id>/', detail_dash, name = "detail_dash"), 
] 
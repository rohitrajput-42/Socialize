from django.shortcuts import render, redirect
from profiles.models import Profile
from .models import Job, Dashboard
from .forms import DashboardForm
from profiles.models import Profile
from .filters import JobFilter

def Jobpage(request):
    customer = Profile.objects.get(user=request.user)
    qs = Job.objects.all()

    myFilter = JobFilter(request.GET, queryset = qs)

    qs = myFilter.qs

    data = {
        'customer': customer,
        'qs': qs,
        'myFilter': myFilter
    }

    return render(request, 'job.html', data)

def JobDetailView(request, id):

    job_form = DashboardForm()
    user = request.user

    if request.method == 'POST':
        job_form = DashboardForm(request.POST or None , request.FILES or None)
        if job_form.is_valid():
            instance = job_form.save(commit = False)
            instance.user = user
            instance.job = Job.objects.get(id = request.POST.get('job_id'))
            instance.job_status = 'Applied'
            instance.save()
        return redirect('job_page')

    data = {}
    data['job_form'] = job_form
    data["job"] = Job.objects.get(id = id) 

    return render(request, 'detail_job.html', data)            


def Jobdashboard(request):
    
    dash = Dashboard.objects.filter(user = request.user)

    data = {
        "dash": dash
    }

    return render(request, "dashboard.html", data)
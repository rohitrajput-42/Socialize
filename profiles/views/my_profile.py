from django.shortcuts import render
from django.views import View
from profiles.models import Profile 
from profiles.forms import ProfileModelForm
from job.models import Dashboard

def My_profile(request): 

    user = request.user

    obj = Profile.objects.get(user=user)

    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=obj)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    data = {

        'obj': obj,
        'form': form,
    }

    return render(request, 'my_profile.html', data)
from django.shortcuts import render, redirect
from profiles.forms import ContactForm

def Contact(request):

    user = request.user

    if request.method == 'POST':
        form = ContactForm(request.POST)
        confirm = False
        
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = user
            instance.save()
            confirm = True 

            return redirect('contact')
        

        data = {
            'form': form,
            'confirm': confirm
        }

        return render(request, "contact.html", data)

    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
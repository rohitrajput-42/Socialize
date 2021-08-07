from django import forms
from .models import Profile, Contact

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'phone', 'message')        
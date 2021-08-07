from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from profiles.models import Profile, Relationship, Career, Contact

class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'created', 'slug', 'email']

class AdminRelationship(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'status']

class AdminContact(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone', 'created']    

admin.site.register(Profile,AdminProfile)
admin.site.register(Relationship, AdminRelationship)
admin.site.register(Career)
admin.site.register(Contact, AdminContact)
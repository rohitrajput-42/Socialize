from django.urls import path
from profiles.views.index import Index
from profiles.views.my_profile import My_profile
from profiles.views.about import About
from profiles.views.contact import Contact

urlpatterns = [
    path('', Index.as_view(), name = "home"),
    path('my_profile', My_profile, name = "my_profile"),
    path('about', About.as_view(), name = "about"),
    path('contact', Contact, name = "contact")
]
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('profiles/', include('profiles.urls')),

    path('', include('posts.urls')),
    
    path('job/', include('job.urls')),

    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
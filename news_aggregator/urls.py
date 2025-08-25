from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.news.urls')),      # Add 'apps.' prefix
    path('users/', include('apps.users.urls')),  # Add 'apps.' prefix
]
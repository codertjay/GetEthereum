from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminmy_url/', admin.site.urls),
]

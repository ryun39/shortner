from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('shortlink.urls')),
    path("account/", include('accountapp.urls')),
]


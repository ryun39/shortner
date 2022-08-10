from django.urls import path, include
from .views import signup

app_name = 'accountapp'
urlpatterns = [
    path("signup/", signup, name="signup"),
]


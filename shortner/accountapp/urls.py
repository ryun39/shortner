from django.urls import path, include
from .views import signup,mylogin, mylogout
from django.contrib.auth import views as auth_views

app_name = 'accountapp'
urlpatterns = [
    path("login/", mylogin.as_view(), name="login"),
    path("logout/", mylogout, name="logout"),
    path("signup/", signup, name="signup"),
]


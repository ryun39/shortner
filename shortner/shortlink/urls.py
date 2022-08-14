
from django.urls import path, include
from .views import index

app_name = 'shortlink'
urlpatterns = [
    path("", index, name='index'),
]



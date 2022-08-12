
from django.urls import path, include
from .views import index, example

app_name = 'shortlink'
urlpatterns = [
    path("", index, name='index'),
    path("example/", example, name='example')

]



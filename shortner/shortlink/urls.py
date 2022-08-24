
from django.urls import path, include
from .views import index, CreateUrl, UpdateUrl

app_name = 'shortlink'
urlpatterns = [
    # path('URL', ViewFunction, 'use in Template')
    path("", index, name='index'),
    path("create/", CreateUrl, name='create'),
    path("update/", UpdateUrl, name='update'),
]
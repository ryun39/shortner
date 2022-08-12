from turtle import settiltangle
from django.shortcuts import render
from django.conf import settings

def index(request):
    print(request.POST)
    return render(request, 'home.html')


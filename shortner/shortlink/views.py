from turtle import settiltangle
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .shorten_url import make_shorten, uri_validator
from django.http.response import HttpResponse


@csrf_protect
def index(request):
    if request.method == "POST":
        data = request.POST
        url = data['s_text']
        if url:
            if uri_validator(url):
                obj = make_shorten(url)
                context = {'sample': obj}
                return render(request, 'home.html', context)
            else:
                w_text = "Please_Try_Again"
                return render(request, 'home.html', {"msg": w_text})
        else:
            return redirect("/")
    else:
        return render(request, 'home.html')

def CreateUrl(request):

    return HttpResponse("in Create Url")

def UpdateUrl(request):

    return HttpResponse("in Update Url")
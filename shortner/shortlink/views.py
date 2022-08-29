from accountapp.models import User
# from shortner.accountapp.models import User
from turtle import settiltangle
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .shorten_url import make_shorten, uri_validator
from django.http.response import HttpResponse
from .models import UserShortenList
from django.contrib.auth.decorators import login_required
from .models import UserShortenList



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

@login_required(login_url='http://127.0.0.1:8000/account/login/')
def CreateUrl(request):
    print(request.user)
    if request.method == "GET":
        return render(request, 'createurl.html')
    elif request.method == "POST":
        data = request.POST

        s_text = data['s_text']

        user = User.objects.get(username=request.user)

        if uri_validator(s_text):
            su = make_shorten(s_text)

        row = UserShortenList(
            user_id = user,
            shorten_url = su.redic_url,
            origin_url = s_text
        )
        row.save()
        context = {'sample': su}
        return render(request, 'createurl.html', context)




def UpdateUrl(request):
    return HttpResponse("in Update Url")
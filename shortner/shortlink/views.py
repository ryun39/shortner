from turtle import settiltangle
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .shorten_url import make_shorten, uri_validator

@csrf_protect
def index(request):
    if request.method == "POST":
        data = request.POST
        url = data['s_text']
        if url:
            if uri_validator(url):
                new_url = make_shorten()
                return render(request, 'home.html', {"sample": new_url})
                # return render(request, redirect('/'), {"sample": new_url})
            else:
                w_text = "Please_Try_Again"
                return render(request, 'home.html', {"msg": w_text})
        else:
            return redirect("/")
    else:
        return render(request, 'home.html')

    # return render(request, 'home.html')


@csrf_protect
def example(request):
    data = request.POST
    url = data['s_text']
    if url:
        if uri_validator(url):
            new_url = make_shorten()
            return render(request, 'home.html', {"sample": new_url})
            # return render(request, redirect('/'), {"sample": new_url})
        else:
            w_text = "Please_Try_Again"
            return render(request, 'home.html', {"msg": w_text})
    else:
        return redirect("/")


import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate

def profile(request):
    if request.method == "GET":
        row = User.objects.get(username=request.user)
        context = {'user_info': row}
        return render(request, 'update.html', context)

def mylogout(request):
    print(request.method)
    logout(request)
    return redirect('/')

class mylogin(View):
    def get(self, request):
        print("in get")
        return render(request, "login.html")
    def post(self, request):
        print("in post")
        data = request.POST
        name = data['lg_username']
        password = data['lg_password']

        if name and password:
            user = authenticate(request, username = name, password = password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/")
        else:
            return HttpResponse("not OK!!")

def signup(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        # 회원정보 DB 저장 로직
        data = request.POST
        
        emailid   = data['emailid']
        pw1       = data['password']
        pw2       = data['cpassword']

        if pw1 != pw2:
            return redirect('/')

        name      = data['mem_name']

        birth_dd  = data['dd']
        birth_mm  = data['mm']
        birth_yy  = data['yyyy']
        birth = birth_yy + "-" + birth_mm + "-" + birth_dd

        gender    = data['gender']
        contact   = data['contactnum']
        payplan   = data['payplan']

        period_dd = data['p_dd']
        period_mm = data['p_mm']
        period_yy = data['p_yyyy']
        period = period_yy + "-" + period_mm + "-" + period_dd

        try :
            user = User.objects.create_user(
            DateOfBirth = birth,
            Gender      = gender,
            Contact     = contact,
            Payplan     = payplan,
            Period      = period,
            email       = emailid,
            password    = pw1,
            username    = name
            )

            
        except IntegrityError:
            return HttpResponse("정보 오류")


        return redirect("/")


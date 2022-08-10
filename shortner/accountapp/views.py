from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from .models import User
from django.db import IntegrityError
import json

# Create your views here.

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


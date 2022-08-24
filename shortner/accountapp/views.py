
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate


def profile(request):
    if request.method == "GET":
        row = User.objects.get(username=request.user)

        dd = str(row.DateOfBirth)
        dd = dd.split('-')

        pp = ""
        if row.Payplan == "Agree":
            pp = str(row.Payplan)
            pp = dd.split('-')

        context = {'user_info':row, "BD":dd, "PP":pp}
        return render(request, 'update.html', context)

def mylogout(request):
    logout(request)
    return redirect('/')

class mylogin(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        data = request.POST
        name = data['lg_username']
        Password = data['lg_password']

        if name and Password:
            user = authenticate(request, username = name, password = Password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                context = {'msg':" 아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다.입력하신 내용을 다시 확인해주세요."}
                return render(request, 'login.html', context)
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

        period = None
        if data['p_dd']:
            print("in preido")
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


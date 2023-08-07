from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def hello_world(request):
    return HttpResponse('Hello,world')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            print('로그인 성공')
            login(request,user) # login 정보 저장
            return redirect('login_user_home')
        else:
            print('로그인 실패')
    
    return render(request, 'login.html')

def home_view(request):
    # 로그인한 사용자 정보
    user = request.user
    context = { # 여러개의 데이터를 바인딩하는 방법
        'username':user.username,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'email':user.email
    }

    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')
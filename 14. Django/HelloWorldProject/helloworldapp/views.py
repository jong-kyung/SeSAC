from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
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
            return redirect('login_user_home')
        else:
            print('로그인 실패')
    
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')
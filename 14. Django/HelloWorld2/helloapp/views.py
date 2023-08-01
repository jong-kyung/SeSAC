from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

def hello_world(request):
    return HttpResponse('Hello World')

def show_message(request):
    # DB로부터 메시지 받아오기, ORM으로 사용하기
    messages = Message.objects.all()

    return render(request, 'message_list.html', {'messages': messages})
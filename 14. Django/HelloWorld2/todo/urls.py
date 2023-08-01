from django.urls import path, include
from todo import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/write', views.todo_write, name='todo_wirte'),
    path('todo/<int:pk>', views.todo_detail, name='todo_detail'),
    path('todo/<int:pk>/delete', views.del_todo, name='dle_todo'),
    path('todo/<int:pk>/update', views.update_todo, name='update_todo')
]
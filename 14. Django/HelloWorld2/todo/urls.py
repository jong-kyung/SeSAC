from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('write/', views.todo_write, name='todo_wirte'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('<int:pk>/delete/', views.del_todo, name='dle_todo'),
    # path('<int:pk>/update/', views.update_todo, name='update_todo')
]
from django.urls import path, include
from vote import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:pk>', views.choice_list, name='choice_list'),
    path('<int:pk>/result/', views.result_choice, name='result_choice'),
]
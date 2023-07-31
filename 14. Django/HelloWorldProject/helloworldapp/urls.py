from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('login/', views.login_view, name = 'login_view'),
    path('home/', views.home_view, name='login_user_home')
]
from django.urls import path, include
from vote import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:pk>', views.choice_list, name='choice_list'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),  
]
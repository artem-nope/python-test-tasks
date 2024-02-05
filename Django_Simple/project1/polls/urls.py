from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('question/detail/<int:pk>/', views.question_detail, name='question-detail'),
    path('question/vote/<int:pk>/', views.question_vote, name='question-vote'),
    path('question/results/<int:pk>/', views.question_results, name='question-results'),
    path('question/add-answer/<int:pk>/', views.add_question_answer, name='add-question-answer'),
    path('question/new-answer/<int:pk>/', views.new_answer, name='new-answer'),
]

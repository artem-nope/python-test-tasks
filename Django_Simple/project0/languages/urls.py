from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("lang/<int:pk>/", views.language_detail, name="language-detail"),
]


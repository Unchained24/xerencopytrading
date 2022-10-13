from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('journal/', views.Journal, name="journal"),
    path('single/<int:pk>/', views.single, name="single" ),
    path('terms/', views.terms, name="terms"),
]
from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.registation, name='register'),
    path('home',views.home,name='home'),
]
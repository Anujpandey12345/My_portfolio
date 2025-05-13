from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='singup'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_user, name='login'),



]
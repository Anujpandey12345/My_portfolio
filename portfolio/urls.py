from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signup, name='home'),
    path('signup/', views.signup, name='singup'),
    path('login/', views.login_user, name='login'),
    path('contact/', views.contact, name='contact'),



]
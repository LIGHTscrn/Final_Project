from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Home/login.html'), name='login'), 
]

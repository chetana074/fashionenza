from django.contrib import admin
from django.urls import path
from fashionenzaApp import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('tryon', views.tryon, name='tryon'),
    path('userInfo', views.userInfo, name='userInfo')
]

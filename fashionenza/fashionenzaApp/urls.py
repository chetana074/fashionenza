from django.contrib import admin
from django.urls import path
from fashionenzaApp import views

urlpatterns = [
    path('', views.index, name='index'), #empty path redirectes to index page
    path('index', views.index, name='index'), #path with 'index' redirectes to index page
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('userInfo', views.userInfo, name='userInfo'),
    path('garments', views.garments, name='garments')
]

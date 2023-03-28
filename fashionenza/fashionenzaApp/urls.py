from django.contrib import admin
from django.urls import path
from fashionenzaApp import views

#Django admin header customization
admin.site.site_header = "Administrator Login"
admin.site.site_title = ""
admin.site.index_title = "Welcome to the Admin Portal"

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('upload', views.upload, name='upload'),
    path('garments', views.garments, name='garments'),
    path('userInfo', views.userInfo, name='userInfo')
]

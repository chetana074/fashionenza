from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def userInfo(request):
    return render(request, 'userInfo.html')

def garments(request):
    return render(request, 'garments.html')
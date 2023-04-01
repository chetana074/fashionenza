from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from fashionenzaApp import imagecapture

def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password1']

        if User.objects.filter(username=username).exists():
            messages.warning(request, "This username is taken")
            return render(request, 'signup.html')
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "This email is taken")
            return render(request, 'signup.html')
        else:
            newUser = User.objects.create_user(username, email, password)
            newUser.first_name = fname
            newUser.last_name = lname
            newUser.save()
            return redirect('signin')
        
    if request.method == "GET": 
        return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            username = user.username
            fname = user.first_name
            # print('loggedIn signin', loggedIn)
            # return render(request, 'home.html', {'fname':fname, 'username':username, 'loggedIn':loggedIn})
            messages.success(request, "User loggedIn!!!")
            return redirect('home')
        else:
            messages.warning(request, "Wrong credentials!! If user is not registered, please sign up first.")
            return redirect('signin')
        
    if request.method == "GET":
        return render(request, 'signin.html')

@login_required
def signout(request):
    logout(request)
    return redirect('welcome')

@login_required
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

@login_required
def about(request):
    if request.method == "GET":
        return render(request, 'about.html')

@login_required
def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')

@login_required
def upload(request):
    if request.method=='POST'and 'your' in request.POST:
       upload=request.FILES['gar']
       fss=FileSystemStorage(location='Garment_by_user')
       fss.save(upload.name, upload)
    if request.method=='POST': 
        up=request.FILES['you']
        fss=FileSystemStorage(location='User_photo')
        fss.save(up.name, up) 
    return render(request,'upload.html')

@login_required
def garments(request):
    return(request,'garments.html')

# def upload(request):
#     if request.method == 'POST' and 'capture' in request.POST: 
#         text = imagecapture.dummy()
#     return render(request,'upload.html') 

@login_required
def userInfo(request):
    return render(request, 'userInfo.html')
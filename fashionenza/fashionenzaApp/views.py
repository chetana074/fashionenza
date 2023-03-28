from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from fashionenzaApp import imagecapture

loggedIn = False

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
            messages.error(request, "This username is taken")
            return render(request, 'signup.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "This email is taken")
            return render(request, 'signup.html')
        else:
            newUser = User.objects.create_user(username, email, password)
            newUser.first_name = fname
            newUser.last_name = lname
            newUser.save()
            messages.success(request, "User registered successfully!!!")
            return redirect('signin')
        
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
            loggedIn = True
            return render(request, 'home.html', {'fname':fname, 'username':username, 'loggedIn':loggedIn})
        else:
            messages.error(request, "User is not registered!!! Please sign up first.")
            return redirect('welcome')
    return render(request, 'signin.html')

def signout(request):
    loggedIn = False
    logout(request)
    return redirect('welcome')

def home(request):
    if(loggedIn):
        return render(request, 'home.html')
    else:
        return redirect('welcome')
    
def about(request):
    if(loggedIn):
        return render(request, 'about.html')
    else:
        return redirect('welcome')

def contact(request):
    if(loggedIn):
        return render(request, 'contact.html')
    else:
        return redirect('welcome')

def upload(request):
    if(loggedIn):
        if request.method == 'POST' and request.FILES['upload']:
            upload = request.FILES['upload']
            fss = FileSystemStorage(location='User_Uploaded_photos')
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            return render(request, 'upload.html', {'file_url': file_url})
        return render(request, 'upload.html')
    else:
        return redirect('welcome')

def garments(request):
    if(loggedIn):
        return(request,'garments.html')
    else:
        return redirect('welcome')

def upload(request):
    if request.method == 'POST' and 'capture' in request.POST: 
        text = imagecapture.dummy()
    return render(request,'garments.html') 

def userInfo(request):
    if(loggedIn):
        return render(request, 'userInfo.html')
    else:
        return redirect('welcome')
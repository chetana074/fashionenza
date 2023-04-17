import os
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
    else : 
        return redirect('signup')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            username = user.username
            fname = user.first_name
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
    if request.method=='POST' and 'your' in request.POST: 
        garmentImg=request.FILES['gar']
        clothImg=request.FILES['you']

        ext1 = os.path.splitext(garmentImg.name)[1]
        ext2 = os.path.splitext(clothImg.name)[1]

        valid_extensions = ['.jpeg','.png','.jpg']

        if (not ext1 in valid_extensions) or (not ext2 in valid_extensions):
            messages.warning(request, "invalid file type")
            return redirect('upload')
        else :
            clothImgSave=FileSystemStorage(location='garment')
            clothImgSave.save(clothImg.name, clothImg)

            garImgSave=FileSystemStorage(location='user')
            garImgSave.save(garmentImg.name, garmentImg)

            return render(request,'final.html')
    else:
        return render(request,'upload.html')

@login_required
def garments(request):
    return(request,'garments.html')

@login_required
def final(request):
    return render(request, 'final.html')

def viton(model_img, cloth_img):
    # run openpose on model_img
    # output - openpose image of model_img

    # run image parse
    # generate h5 file and store in imageparse folder
    # load that file here and run that file
    # output - imageparse of model_img

    # run cloth mask - run py file from Clothmask folder
    # output - clothmask of cloth_img

    # run viton file - test.py from viton folder
    # viton contains everything - networks.py, test.py etc etc
    # output - superimposed image
    return 
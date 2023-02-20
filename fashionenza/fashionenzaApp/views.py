from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def welcome(request):
    return render(request, 'welcome.html')

def validate_password(s):
    l, u, p, d = 0, 0, 0, 0
    if (len(s) >= 8):
        for i in s:
            
            # counting lowercase alphabets
            if (i.islower()):
                l+=1           
    
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
    
            # counting digits
            if (i.isdigit()):
                d+=1           
    
            # counting the mentioned special characters
            if(i=='@'or i=='$' or i=='_'):
                p+=1          

    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
        return True
    else:
        return False
    
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        newUser = User.objects.create_user(username, email, password1)
        newUser.first_name = fname
        newUser.last_name = lname
        newUser.save()

        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'home.html', {'fname':fname})
        else:
            return redirect('welcome')

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('welcome')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tryon(request):
    return render(request, 'tryon.html')

def userInfo(request):
    return render(request, 'userInfo.html')
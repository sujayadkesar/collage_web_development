from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.user.is_active:
        messages.warning(request, "your are already logged in")
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request ,username=name, password=passwd)
            print(name,passwd)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                print("hi")
                return redirect("/")
            else:
                messages.error(request, "invalid username and password")
                a="username and password is error"
                return redirect("/")
        
        return render(request, "registration/Login.html")
    
def homepage(request):
    return render(request, "home.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
                return redirect("home")
            else:
                messages.error(request, "invalid username and password")
                a="username and password is error"
                return redirect("/")
        
        return render(request, "registration/Login.html")
    

def change_password(request):
    context={}
    ch = User.objects.filter(id=request.user.id)
    if len(ch)>0:
        data = User.objects.get(id=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"change_password.html",context)
from django.shortcuts import render
from .models import newsletter
from django.contrib import messages
from account.models import Profile
from django.contrib.auth.models import User
# Create your views here.


def homepage(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
    
        if request.method == "POST":
            email = request.POST.get('email')
            if not newsletter.objects.filter(email=email).exists() :
                email_instance = newsletter.objects.create(email=email)
            else:
                messages.error(request, 'Email already exists')
            
        context = {
            'profile': profile
        }
            
        return render(request,"index.html",context)
    return render(request,"index.html")

def profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        profile = Profile.objects.get(user=user)
        context = {
            'profile': profile
        }
        return render(request,'profile.html',context)
from django.shortcuts import render
from .models import newsletter
from django.contrib import messages
# Create your views here.


def homepage(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        if not newsletter.objects.filter(email=email).exists() :
            email_instance = newsletter.objects.create(email=email)
        else:
            messages.error(request, 'Email already exists')
            
            
            
    return render(request,"index.html")
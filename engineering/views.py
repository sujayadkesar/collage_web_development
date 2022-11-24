from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import NoticeBoard_Engineering,Events


# Create your views here.
def engineering_homepage(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        news = NoticeBoard_Engineering.objects.all().order_by('-id')
        Event = Events.objects.all().order_by('-id')[:3]
        context={
            "news":news,
            "event":Event
        }
        if user.groups.filter(name= 'engineering').exists():
            return render(request, 'engineering/engineering.html', context)
        else :
            return redirect('home')
    else:
        return redirect('login')

def engineering_event_page(request):
    Event = Events.objects.all().order_by('-id')
    context={
        "event":Event
    }
    return render(request, 'engineering/events.html',context)

def cs_department(request):
    return render(request,'engineering/departments/csdepartment.html')

def engineering_event_page_details(request,name):
    Event = Events.objects.filter(Title=name)
    context={
        "event":Event
    }
    return render(request, 'engineering/events_details.html',context)
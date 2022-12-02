from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import NoticeBoard_Engineering,Events,Faculty
from django.contrib.auth.decorators import login_required



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
        
        return render(request, 'engineering/engineering.html', context)
    else:
        return redirect('login')

@login_required(redirect_field_name='login')
def engineering_event_page(request):
    Event = Events.objects.all().order_by('-id')
    context={
        "event":Event
    }
    return render(request, 'engineering/events.html',context)

@login_required(redirect_field_name='login')
def cs_department(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        return render(request,'engineering/departments/csdepartment.html')
    else:
        return redirect('error')

@login_required(redirect_field_name='login')
def engineering_event_page_details(request,name):
    Event = Events.objects.filter(Title=name)
    context={
        "event":Event
    }
    return render(request, 'engineering/events_details.html',context)

@login_required(redirect_field_name='login')
def cs_department_overview(request):
    user = User.objects.get(username=request.user.username)
    if user.groups.filter(name= 'engineering').exists():
        faculty = Faculty.objects.all()
        context = {
            'faculty':faculty
        }
        return render(request, 'engineering/departments/overview/cs_overview.html', context)
    else:
        return redirect('error')

def error(request):
    return render(request,'engineering/error/error.html')


def contact(request):
    return render(request,'engineering/contact/index.html')


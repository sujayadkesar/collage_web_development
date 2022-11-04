
from django.urls import path, include
from .views import Login, homepage

urlpatterns = [
    path('login', Login, name='login'),
    
]

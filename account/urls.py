
from django.urls import path, include
from .views import Login

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    
]


from django.urls import path, include
from .views import Login, change_password

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/changepassword",change_password, name="changepassword" ),
]

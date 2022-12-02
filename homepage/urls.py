from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="home"),
    path('profile',views.profile,name="profile"),
    path('gallery',views.gallery,name="gallery"),
    path('about us',views.about,name="about"),
]

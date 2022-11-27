from django.urls import path
from . import views

urlpatterns = [
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY', views.engineering_homepage, name='engineering'),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/Events', views.engineering_event_page, name='engineering_events' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/CS Department', views.cs_department, name='cs_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/Events/<name>', views.engineering_event_page_details, name='engineering_events_details' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/CS Department/overview', views.cs_department_overview, name='cs_department_overview'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.school_admin_home),
    path('addstudent',views.school_admin_addstudent),
    path('viewstudent',views.school_admin_viewtudent),
    path('viewattendence',views.school_admin_viewattendence),
       
]

from django.urls import path
from . import views

urlpatterns = [
    path('home', views.teacher_home),
    path('addattendence',views.teacher_addattendence),
    path('viewstudent',views.teacher_viewstudent),
    path('profile',views.teacher_profile),
]    
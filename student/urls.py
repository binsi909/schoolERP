from django.urls import path
from . import views

urlpatterns = [
    path('home', views.student_home),
    path('changepassword',views.student_changepassword),
    path('profile',views.student_profile),
    path('viewattendence',views.student_viewattendence),
       
]

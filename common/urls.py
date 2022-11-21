from django.urls import path
from . import views
app_name ='common'

urlpatterns = [
    path('admin_login',views.admin_login ,name='adlogin'),
    path('student_login',views.student_login ,name='stlogin'),
    path('tbbbrlogin',views.teacher_login,name='trlogin'),
    path('home',views.home ,name='homepage'),

]
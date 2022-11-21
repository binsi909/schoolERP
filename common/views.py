from django.shortcuts import render

# Create your views here.
def admin_login(request):
   return render(request,'common_templates/admin_login.html')
   
def teacher_login(request):
   return render(request,'common_templates/teacher_login.html')
def student_login(request):
   return render(request,'common_templates/student_login.html')
def home(request):
   return render(request,'common_templates/home.html')   

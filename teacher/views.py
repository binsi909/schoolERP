from django.shortcuts import render

# Create your views here.
def teacher_home(request):
    return render(request, 'teacher_templates/home.html')
def teacher_addattendence(request):
    return render(request,'teacher_templates/addattendence.html')
def teacher_viewstudent(request):
    return render(request,'teacher_templates/viewstudent.html')
def teacher_profile(request):
    return render(request,'teacher_templates/profile.html')

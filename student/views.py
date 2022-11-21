from django.shortcuts import render

# Create your views here.
def student_home(request):
    return render(request, 'student_templates/home.html')
def student_profile(request):
    return render(request, 'student_templates/profile.html')
def student_changepassword(request):
    return render(request, 'student_templates/changepassword.html')
def student_viewattendence(request):
    return render(request,'student_templates/viewattendence.html')

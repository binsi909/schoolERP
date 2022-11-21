from django.shortcuts import render

# Create your views here.
def school_admin_home(request):
    return render(request, 'school_admin_templates/home.html')
def school_admin_addstudent(request):
    return render(request, 'school_admin_templates/addstudent.html')
def school_admin_viewtudent(request):
    return render(request, 'school_admin_templates/viewstudent.html')
def school_admin_viewattendence(request):
    return render(request,'school_admin_templates/viewattendence.html')

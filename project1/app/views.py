from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Course

def home(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse('Contact page')

def about(request):
    return HttpResponse('about')

def students(request):
    students_data = Student.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        course_id = request.POST['course']
        if course_id:
            course = Course.objects.get(id=course_id)
            students_data = Student.objects.filter(course = course)
    return render(request, 'pages/students1.html',{'students':students_data,'courses':courses})


def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'pages/student.html',{"student":student})
   

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
       
        student = Student.objects.create(name=name,course=course,sid=sid)
        student.save()
        return redirect("students")
    return render(request,'pages/add_student.html')

def edit_student(request,sid):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
        student.name=name
        student.course=course
        student.sid=sid
        student.save()
       
    return render(request,'pages/edit_student.html',{'student':student})


def delete_student(request, sid):
   
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("students")
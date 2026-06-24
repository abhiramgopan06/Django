from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Course
from .forms import AddCourseForm

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
    courses = Course.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        course = Course.objects.get(id = request.POST['course'])

        sid = request.POST['sid']
        student = Student.objects.create(name=name,course=course,sid=sid)
        student.save()
        return redirect("students")
    return render(request,'pages/add_student.html',{'courses':courses})

def edit_student(request,id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
        student.name=name
        student.course = Course.objects.get(id=course_id)
        student.sid=sid
        student.save()
        return redirect("students")
    return render(request,'pages/edit_student.html',{'student':student,'courses':courses})


def delete_student(request, sid):
   
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("students")


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = AddCourseForm()
    return render(request,
                  'courses/add_course.html',
                  {'fotm':form}
                  )
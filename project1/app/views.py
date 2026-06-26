from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import Student,Course
from .forms import AddCourseForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse('Contact page')

def about(request):
    return HttpResponse('about')

def students(request):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        students_data = Student.objects.all()
        courses = Course.objects.all()
        if request.method == 'POST':
            course_id = request.POST['course']
            if course_id:
                course = Course.objects.get(id=course_id)
                students_data = Student.objects.filter(course = course)
        return render(request, 'pages/students1.html',{'students':students_data,'courses':courses})
    else:
        return redirect('login')

@login_required
def get_student(request,id):
    student = Student.objects.get(id=id)
    return render(request,'pages/student.html',{"student":student})
   
@login_required
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

@login_required
def edit_student(request,id):
    student = Student.objects.get(id=id)
    courses = Course.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
        student.name=name
        student.course = Course.objects.get(id=course)
        student.sid=sid
        student.save()
        return redirect("students")
    return render(request,'pages/edit_student.html',{'student':student,'courses':courses})

@login_required
def delete_student(request, sid):
   
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("students")

@login_required
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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if password == cpassword:
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email
            )
            user.save()
            return redirect('login')
        else:
            return render(request,'auth/register.html',{'error':"Password mismatch"})
    return render(request, 'auth/register.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('students')
            else:
                return redirect('login')
    return render(request,'auth/login.html',{'form':form})     

def logout_view(request):
    logout(request)
    return redirect('login')   
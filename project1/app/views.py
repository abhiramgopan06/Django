from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
students_list = [
    # {"name": "Alan", "course": "BSC", "sid": 0},
    # {"name": "Kavin", "course": "MSC", "sid": 1},
    # {"name": "Leivin", "course": "BCA", "sid": 2},
    # {"name": "Jaison", "course": "BTECH", "sid": 3},
    # {"name": "Abin", "course": "MCA", "sid": 4},
    # {"name": "Sam", "course": "MBA", "sid": 5},
    # {"name": "Tom", "course": "MA", "sid": 6},
    # {"name": "Jithu", "course": "BSC", "sid": 7}
]
def home(request):
    return render(request, 'index.html')

def contact(request):
    return HttpResponse('Contact page')

def about(request):
    return HttpResponse('about')

def students(request):
    return render(request, 'pages/students1.html',{'students':students_list})

# def students(request):
#     return HttpResponse('Students')

# def get_student(request,sid):
#     print(sid)
#     return HttpResponse(f"Name : {students_list[sid]['name']['course']}")
    # return HttpResponse(f"Student : {students_list[id]}")
def get_student(request,id):
    print(id)
    print(students_list[id]['course'])
    print(students_list[id]['sid'])
    return render(request,'pages/student.html',{"name":students_list[id]['name'],"course": students_list[id]['course'],"sid": students_list[id]['sid']})

def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
        students_list.append({
            "name":name,
            "course":course,
            "sid":sid
        })
        return redirect("students")
    return render(request,'pages/add_student.html')

def edit_student(request,sid):
    if request.method == "POST":
        name = request.POST['name']
        course = request.POST['course']
        sid = request.POST['sid']
        for x in students_list:
            if x['sid'] == sid:
                x['name'] = name
                x['course'] = course
                return redirect("students")
    student =""
    for x in students_list:
        if x['sid'] == sid:
            student = x

    return render(request,'pages/edit_student.html',{'student':student})


def delete_student(request, sid):
    for x in students_list:
        if x['sid'] == sid:
            students_list.remove(x)
            return redirect("students")

    return redirect("students")
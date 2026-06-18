from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('students/',views.students,name="students"),
    # path('student/<int:sid>/',views.get_student),
    path('student/<int:id>/',views.get_student,name="get_student"),
    path('add/',views.add_student,name="add_student"),
    path('edit/<int:sid>/',views.edit_student,name="edit_student"),
    path('delete/<str:sid>/', views.delete_student, name='delete_student'),

]
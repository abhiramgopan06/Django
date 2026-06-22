from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=25)
    def _str_(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=25)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    sid = models.CharField(unique=True)

    def _str_(self):
        return self.name
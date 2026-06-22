from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=25)
    course = models.CharField(max_length=20)
    sid = models.CharField(unique=True)

    def _str_(self):
        return self.name
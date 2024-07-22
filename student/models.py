from django.db import models
import datetime

class Student(models.Model):
    student_name=models.CharField(max_length=40)
    Student_bio=models.TextField()
    student_email=models.EmailField()
    student_nationality=models.CharField(max_length=20)
    date_of_birth=models.DateTimeField(datetime.date, blank = True)
    student_Guardian=models.CharField(max_length=40)
    student_class = models.CharField(max_length=20)
    student_mentor=models.CharField(max_length=40)




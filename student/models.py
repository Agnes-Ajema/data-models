from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=40)
    Student_bio=models.TextField()
    student_email=models.EmailField()
    student_nationality=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    student_code = models.IntegerField()
    student_Guardian=models.CharField(max_length=40)
    student_locker_number=models.IntegerField()
    student_class = models.CharField(max_length=20)
    student_mentor=models.CharField(max_length=40)

    def __str__(self):
       return f"{self.first_name}{self.last_name}"


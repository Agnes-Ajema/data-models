from django.db import models

# Create your models here.

class Teachers (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    age= models.PositiveSmallIntegerField()
    email= models.EmailField(max_length=20)
    nationality = models.CharField(max_length=20)
    course= models.CharField(max_length=20)
    national_id= models.PositiveSmallIntegerField()
    years_of_experience= models.PositiveSmallIntegerField()
    teaching_hours=models.PositiveSmallIntegerField()

def __str__(self):
       return f"{self.first_name}{self.last_name}"








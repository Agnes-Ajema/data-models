from django.db import models

# Create your models here.
class Courses (models.Model):
    course_name = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
    duration=models.IntegerField()
    assessments= models.IntegerField()
    syllabus= models.CharField(max_length=20)
    assignment= models.IntegerField()
    course_id= models.IntegerField()
    description= models.TextField(max_length=200)
    prerequisites= models.CharField(max_length=20)
    resources=models.CharField(max_length=20)
from django.db import models

# Create your models here.
class Courses (models.Model):
    course_name = models.CharField(max_length=20)
    trainer = models.CharField(max_length=20)
    duration=models.DurationFieldField()
    number_of_assessments= models.IntegerField()
    syllabus= models.TextField()
    number_of_assignment= models.IntegerField()
    course_id= models.IntegerField()
    description= models.TextField()
    requirements= models.TextField()
    teaching_materials=models.TextField()
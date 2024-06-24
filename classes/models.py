from django.db import models

# Create your models here.
class Class (models.Model):
    class_name = models.CharField(max_length=20)
    class_electronic_items = models.TextField()
    class_capacity=models.PositiveSmallIntegerField()
    class_motto= models.TextField()
    class_groups= models.TextField()
    no_of_tables = models.IntegerField()
   no_of_chairs= models.IntegerField()
    class_lessons= models.TextField()
    class_student_representative= models.CharField()
    class_size=models.CharField(max_length=20)
  

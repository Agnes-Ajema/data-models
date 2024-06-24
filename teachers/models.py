from django.db import models

# Create your models here.

class Teachers (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    Date_of_Birth= models.IntegerField()
    email= models.EmailField()
    Account_Number= models.PositiveLargeIntegerField()
    national_id= models.PositiveLargeIntegerField()
    phone_number= models.IntegerField()
    teaching_hours=models.DurationField()

def __str__(self):
       return f"{self.first_name}{self.last_name}"








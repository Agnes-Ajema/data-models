
from rest_framework import serializers
from student.models import Student
from classperiod.models import ClassPeriod
from teachers.models import Teachers
from courses.models import Courses
from classes.models import Class




class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Student
       fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
   class Meta:
       model = Courses
       fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
   class Meta:
       model = Class
       fields = '__all__'


class ClassPeriodSerializer(serializers.ModelSerializer):
   class Meta:
       model = ClassPeriod
       fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
   class Meta:
       model = Teachers
       fields = '__all__'

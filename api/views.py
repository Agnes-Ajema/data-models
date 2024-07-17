from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from courses.models import Courses
from classes.models import  Class
from classperiod.models import  ClassPeriod
from teachers.models import Teachers
from .serializers import TeacherSerializer, ClassPeriodSerializer, ClassSerializer, StudentSerializer, CourseSerializer
from rest_framework.response import Response


# Create your views here.
class StudentListView(APIView):
    def get(self, request):
       students = Student.objects.all()
       serializer = StudentSerializer(students, many=True)
       return Response(serializer.data)


class CoursesListView(APIView):
   def get(self, request):
       coursess = Courses.objects.all()
       serializer= CourseSerializer(coursess,many=True)
       return Response(serializer.data)


class TeacherListView(APIView):
   def get(self, request):
       teachers= Teacher.objects.all()
       serializer= TeacherSerializer(teachers,many=True)
       return Response(serializer.data)


class ClassListView(APIView):
   def get(self, request):
      classess = Class.objects.all()
      serializer= ClassSerializer(classess,many=True)
      return Response(serializer.data)


class ClassPeriodListView(APIView):
   def get(self, request):
      classperiod = ClassPeriod.objects.all()
      serializer= ClassPeriodSerializer(classperiod, many=True)
      return Response(serializer.data)

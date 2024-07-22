from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from courses.models import Courses
from classes.models import  Class
from classperiod.models import  ClassPeriod
from teachers.models import Teachers
from .serializers import TeacherSerializer, ClassPeriodSerializer, ClassSerializer, StudentSerializer, CourseSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class StudentListView(APIView):
    def get(self, request):
       student = Student.objects.all()
       serializer = StudentSerializer(student, many=True)
       return Response(serializer.data)

    def post(self, request):
      serializers = StudentSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class CoursesListView(APIView):
   def get(self, request):
       coursess = Courses.objects.all()
       serializer= CourseSerializer(coursess,many=True)
       return Response(serializer.data)

   def post(self, request):
      serializers = CourseSerializer(datarequest.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def get(self,request,id):
        courses=Course.objects.get(id=id)
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    def put (self,request,id):
        courses=Course.objects.get(id=id)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        courses=Course.objects.get(id=id)
        Course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

class TeacherListView(APIView):
   def get(self, request):
       teachers= Teacher.objects.all()
       serializer= TeacherSerializer(teachers,many=True)
       return Response(serializer.data)

   def post(self, request):
      serializers = TeacherSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self,request,id):
        teachers=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Teacher)
        return Response(serializer.data)
    def put (self,request,id):
        teachers=Teacher.objects.get(id=id)
        serializer=TeacherSerializer(Teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teachers=Teacher.objects.get(id=id)
        teachers.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

class ClassListView(APIView):
   def get(self, request):
      classess = Class.objects.all()
      serializer= ClassSerializer(classess,many=True)
      return Response(serializer.data)
   def post(self, request):
      serializers = ClassSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class ClassPeriodListView(APIView):
   def get(self, request):
      classperiod = ClassPeriod.objects.all()
      serializer= ClassPeriodSerializer(classperiod, many=True)
      return Response(serializer.data)
   def post(self, request):
      serializers = ClassPeriodSerializer(data=request.data)
      if serializers.is_valid():
         serializers.save()
         return Response(serializers.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
   def put(self,request,id):
      student=Student.objects.get(id=id)
      serializer=StudentSerializer(student,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   def delete(self,request,id):
      student= Student.objects.get(id=id)
      student.delete()
      return Response(status=status.HTTP_202_ACCEPTED)



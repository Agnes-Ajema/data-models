from django.shortcuts import render
from rest_framewok.views import APIView
from student.models import student
from serializers import StudentSerializer
from .models import Course, Classroom, ClassPeriod
from .serializer import CourseSerializer,ClassroomSerializer,ClassPeriodSerializer
from rest_framewok.response import response

# Create your views here.
class StudentListView(APIView):
     def get(self,request):
        student = student.objects.all()
        serializer = StudentSerializer(students, many=true)
        return Response(serializer.data)

class CourseListView(APIView):
    Course = Course.objects.all()
    serializer= CourseSerializer(course,many=true)
    return Response(serializer.data)

class ClassroomListView(APIView):
    Classroom = Classroom.objects.all()
    serializer= ClassroomSerializer(classroom,many=true)
    return Response(serializer.data)

class ClassPeriodListView(APIView):
    ClassPeriod= ClassPeriod.objects.all()
    serializer= ClassPeriodSerializer(ClassPeriod,many=true)
    return Response(serializer.data)
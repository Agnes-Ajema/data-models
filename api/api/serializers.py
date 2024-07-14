from root-framewok import serializers
from student.models import Student
from ClassPeriod.models import Course, classroom, ClassPeriod

class StudentSerializer(serializers.ModelSerializer):
       class Meta:
             model = student
             fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = '__all__'
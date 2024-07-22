from django.urls import path
from .views import StudentListView,CoursesListView,ClassListView,ClassPeriodListView,TeacherListView,TeacherDetailView,CourseDetailView
from .views import StudentDetailView


urlpatterns = [
   path("students/", StudentListView.as_view(),name="student_list_view"),
   path("courses/", CoursesListView.as_view(), name="course_list_view"),
   path("classes/", ClassListView.as_view(), name="classes_list_view"),
   path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
   path("classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view"),
   path("students/<int:id>/",StudentDetailView.as_view(),name="student_detail_view"),
   path("course/<int:id>/" ,CourseDetailView.as_view(),name="course_detail_view"), 
   path("teacher/<int:id>/" ,TeacherDetailView.as_view(),name="teacher_detail_view"),
]

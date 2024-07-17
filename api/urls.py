from django.urls import path
from api.views import StudentListView,CoursesListView,ClassListView,ClassPeriodListView,TeacherListView


urlpatterns = [
   path("student/", StudentListView.as_view(),name="student_list_view"),
   path("courses/", CoursesListView.as_view(), name="course_list_view"),
   path("classes/", ClassListView.as_view(), name="classes_list_view"),
   path("teachers/", TeacherListView.as_view(), name="teacher_list_view"),
   path("classperiod/", ClassPeriodListView.as_view(), name="classperiod_list_view")
]

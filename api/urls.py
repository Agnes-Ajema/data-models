from django.urls import Path
from .views import StudentListView,CourseListView,ClassroomListView,ClassPeriodListView

urlpatterns=[
    path('students/', StudentListView.as_view(),name='student_list_view'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('classrooms/', ClassroomListView.as_view(), name='classroom-list'),
    path('class-periods/', ClassPeriodListView.as_view(), name='class-period-list')
]
from django.urls import path
from .views import TeacherDetailView,AddTeacherView,UpdateTeacher

app_name = 'admin'

urlpatterns = [
    path('admin/teacher_page/',TeacherDetailView.as_view(),name='admin_teacher'),
    path('admin/add_teacher/',AddTeacherView.as_view(),name='add_teacher'),
    path('admin/update_teacher/<int:pk>/',UpdateTeacher.as_view(),name='update_teacher')
]
from django.urls import path
from .views import TeacherDetailView,AddTeacherView,UpdateTeacher,teacher_list

app_name = 'admin_page'

urlpatterns = [
    path('admin/teacher_list/',teacher_list,name='admin_home'),
    path('admin_page/teacher_detail/<int:pk>/',TeacherDetailView.as_view(),name='teacher_detail'),
    path('admin_page/add_teacher/',AddTeacherView.as_view(),name='add_teacher'),
    path('admin_page/update_teacher/<int:pk>/',UpdateTeacher.as_view(),name='update_teacher')
]
from django.urls import path
from .views import admin_page

app_name = 'admin'

urlpatterns = [
    path('admin/teacher_page/',admin_page,name='admin_teacher')
]
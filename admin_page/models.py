from django.db import models
from user.models import CustomUser


Role = (
        ('admin_page', 'Admin'),
        ('seller', 'Seller'),
        ('teacher','Teacher')
    )
class Teacher(models.Model):
    username = models.CharField(max_length=55)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=55)
    role  = models.CharField(max_length=20, choices=Role, default='teacher')


class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='students')
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.CharField(max_length=50)


class GroupStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    salary_data = models.DateField()
    for_month = models.DateField()
    salary_type = models.CharField(max_length=50)

class Paymet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField()
    paymet_data = models.DateField()
    for_month = models.DateField()
    payment_type = models.CharField(max_length=50)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=55)


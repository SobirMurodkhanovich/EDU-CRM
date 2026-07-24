from django import forms
from .models import Teacher, Student


class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('username','first_name','last_name','phone','password')

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name','phone')

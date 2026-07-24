from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AddTeacherForm, AddStudentForm
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers':teachers
    }
    return render(request, 'admin/teacher/techer_page.html',context)

class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        students = teacher.students.all()
        context = {
            'teacher': teacher,
            'students': students
        }
        return render(request, 'admin/teacher/teacher-detail.html', context)


class AddTeacherView(View):
    def get(self, request):
        form = AddTeacherForm()
        context = {'form': form}
        return render(request, 'admin/teacher/add-teacher.html', context)

    def post(self, request):
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page:admin_home')
        context = {'form': form}
        return render(request, 'admin/teacher/add-teacher.html', context)


class UpdateTeacher(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = AddTeacherForm(instance=teacher)
        context = {'form': form, 'teacher': teacher}
        return render(request, 'admin/teacher/update-teacher.html', context)

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = AddTeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('admin_page:admin_home')
        context = {'form': form, 'teacher': teacher}
        return render(request, 'admin/teacher/update-teacher.html', context)









# ============================ Student Section ============================





class StudentView(View):
    def get(self, request):
        return render(request, 'admin/student/student_page.html')

class  AddStudentView(View):
    def get(self, request):
        form = AddStudentForm()
        context = {'form': form}
        return render(request, 'admin/student/add_student.html', context)

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_page:student_page')
        context = {'form': form}
        return render(request, 'admin/student/add_student.html', context)

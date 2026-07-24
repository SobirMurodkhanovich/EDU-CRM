from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AddTeacherForm
from .models import Teacher


class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        students = teacher.student_set.all()
        context = {
            'teacher': teacher,
            'students': students
        }
        return render(request, 'admin/teacher/techer_page.html', context)


class AddTeacherView(View):
    def get(self, request):
        form = AddTeacherForm()
        context = {'form': form}
        return render(request, 'add-teachet.html', context)

    def post(self, request):
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:admin_home')
        context = {'form': form}
        return render(request, 'add-teachet.html', context)


class UpdateTeacher(View):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = AddTeacherForm(instance=teacher)
        context = {'form': form, 'teacher': teacher}
        return render(request, 'update-teacher.html', context)

    def post(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        form = AddTeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        context = {'form': form, 'teacher': teacher}
        return render(request, 'update-teacher.html', context)


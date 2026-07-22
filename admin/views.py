from django.shortcuts import render

def admin_page(request):
    return render(request,'admin/teacher/teacher_page.html')

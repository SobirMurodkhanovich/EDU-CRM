from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm,LoginUserForm,UserProfileUpdateForm

class RegisterView(View):
    def get(self,request):
        form = RegisterUserForm()
        context = {
            'form':form
        }
        return render(request,'user/register.html',context)
    def post(self,request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
        return render(request, 'user/register.html')

class LoginView(View):
    def get(self,request):
        form = LoginUserForm()
        context = {
            'form':form
        }
        return render(request,'user/login.html',context)

    def post(self,request):
        if request.method == 'POST':
            form = LoginUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.type_staff == 'admin':
                        return redirect('admin_home')
                    elif user.type_staff == 'seller':
                        return redirect('seller_home')
                else:
                    return render(request, 'user/login.html', {'form': form, 'error': 'Invalid credentials.'})
        else:
            form = LoginUserForm()

        return render(request, 'user/login.html', {'form': form})

def admin_home(request):
    return render(request, 'admin/teacher/techer_page.html')

class UserProfile(View):
    def get(self,request):
        user = request.user
        context = {
            'user':user,
        }
        return render(request,'user/profile.html',context)


class UpdateProfileView(View):
    def get(self, request):
        form = UserProfileUpdateForm(instance=request.user)
        context = {'form': form}
        return render(request, 'user/update-profile.html', context)

    def post(self, request):
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')

        context = {'form': form}
        return render(request, 'user/update-profile.html', context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing_page')
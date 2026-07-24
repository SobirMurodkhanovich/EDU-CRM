
from django.urls import path


from .views import RegisterView, LoginView, LogoutView, UserProfile, UpdateProfileView,admin_home

app_name ='user'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('admin_home/', admin_home, name='admin_home'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', UserProfile.as_view(), name='profile'),
    path('update_profile', UpdateProfileView.as_view(), name='update_profile'),

]
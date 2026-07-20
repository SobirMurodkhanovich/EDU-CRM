from django import forms
from .models import CustomUser

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password')

    def save(self,commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

class LoginUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','password')

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email', 'phone')

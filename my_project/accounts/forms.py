from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User
from .models import UserProfile


# this is django form.UserCreationForm automatically handles password hashing. provides built-in validation for password strength.check existing user.email etc
class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = CustomUser     # Use the CustomUser model for user registration(created at models.py file)
        fields = ['username', 'email', 'user_type', 'password1', 'password2']  


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class UserProfileForm(forms.ModelForm):
    skills = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Skills (comma-separated)"}))

    class Meta:
        model = UserProfile
        fields = ["phone", "job_title", "bio", "skills", "profile_picture", "location", "video", "language", "education", 'github_link', "linkedin_link", "project_link"]
        

 

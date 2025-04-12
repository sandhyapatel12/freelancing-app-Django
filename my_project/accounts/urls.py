
from django.contrib import admin
from django.urls import path, include
from .views import register_view, login_view, logout_view, socialLoader_view, switch_role,profile, edit_profile
from django.contrib.auth.views import LogoutView



app_name = "accounts"  # ✅ Add this to register the namespace


urlpatterns = [
    
    path("register/", register_view, name='register'),
    path("login/", login_view, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),  # ✅ Use Django's LogoutView
    path("social-loader/", socialLoader_view, name='social-loader'),
    path("switch-role/", switch_role, name="switch_role"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),

]


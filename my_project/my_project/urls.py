"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def redirect_to_home_or_login(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect to home if logged in
    return redirect("accounts:login")  # Otherwise, redirect to login



urlpatterns = [
    path("admin/", admin.site.urls),                # admin
    path('accounts/', include('accounts.urls')),    # account app
    path('accounts/', include('allauth.urls')),     # Add this line to include allauth routes(in this accounts is not my app name. this is by default from allauth)
    path('', include('main.urls')),                 # Connect main app
    path("", redirect_to_home_or_login, name="root"),  # Redirect based on auth status


    path("__reload__/", include("django_browser_reload.urls")),   #   add also last (this autoreload is not need in production)

]


# Add this at the end
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# in simple term views.py is Brain of your website.It decides what to show and what to do.
# The views.py file is used to write the logic of your website or web app.
# When someone opens your website or clicks a button, Django will run the code written in views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import logging
from .models import CustomUser  # Import CustomUser instead of default User
from django.http import JsonResponse
from .forms import UserForm, UserProfileForm
from .models import CustomUser, UserProfile  # ✅ Add this
from .forms import UserForm, UserProfileForm  # ✅ Ensure forms are imported
from django.contrib import messages





# Create your views here.

# Configure logging
logger = logging.getLogger(__name__)    # for debugging error msg(print msg on console)

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)  # Create form instance with POST data

        if form.is_valid():   # validate form data
            user = form.save()   # save new user
            # login user automatically
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")    # in this app we use two backends 1.default 2.allauth so here requierd to mention whih is used for registration 
            request.session["show_loader"] = True   #   if registration successfully then display loader
            return redirect("accounts:register")  # First, reload the registration page to show the loader

    else:
        form = CustomUserCreationForm()   # # If GET request, show an empty form    so user can fill the form

    # Clear session variable after rendering the page
    show_loader = request.session.pop("show_loader", False)  #The pop method is used to remove a value from the session and return it.
    
    # Render the registration page with the form and loader status(so we can use in a fronted)
    return render(request, "accounts/register.html", {"form": form, "show_loader": show_loader})


def login_view(request):
    username_error = None
    password_error = None

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # First, check if the username exists in the database
        try:
            user = CustomUser.objects.get(username=username)   # customUser we create at models file
        except CustomUser.DoesNotExist:
            # If the username doesn't exist in the database
            username_error = "Username not found"
        else:
            # If the username exists, try to authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                request.session["show_loader"] = True
                return redirect("accounts:login")  # Redirect to login
            else:
                password_error = "Incorrect password"  # Authentication failed due to incorrect password

    # Clear session variable after rendering the page
    show_loader = request.session.pop("show_loader", False)

    return render(request, "accounts/login.html", {
        "show_loader": show_loader,
        "username_error": username_error,
        "password_error": password_error
    })

@login_required
def logout_view(request):
    logger.info(f"User {request.user.username} logged out")
    logout(request)
    return redirect('accounts:login')


def socialLoader_view(request):
    return render(request, 'accounts/social-loader.html' )

@login_required
def switch_role(request):
    
    #Toggle user role between Freelancer and Client
    user = request.user  # Get the current logged-in user
    
    # Toggle between freelancer and client
    if user.user_type == "freelancer":
        user.user_type = "client"
    else:
        user.user_type = "freelancer"
    
    user.save()  # Save the updated role in the database

    # Return a JSON response for fetch request
    return JsonResponse({"status": "success", "new_role": user.user_type})



@login_required
def edit_profile(request):
    # Ensure the profile exists before accessing it
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=profile)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print(request.FILES)

            messages.success(request, "Profile updated successfully!")
            return redirect("accounts:profile")

    return render(request, "accounts/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })



@login_required
def profile(request):
    profile = request.user.profile  # or use get_object_or_404 if unsure
    return render(request, "accounts/profile.html", {
        "profile": profile
    })






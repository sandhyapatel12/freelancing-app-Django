# model file Handles database operations.
# A model in Django is a Python class that defines the structure of a database table.
# It is used to create, read, update, and delete data in the database using Django's ORM (Object Relational Mapping).

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

# create table in database : CustomUser but Django uses by default Users table so display in admin panel Users table not CustomUser
class CustomUser(AbstractUser):  #When you inherit from AbstractUser, all the default fields (like username, email, and password) are already included in the model

    # type defining
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer'),
    )

    email = models.EmailField(unique=True)  # ✅ Add this line

    # add one custom field because this is not provied by abstract class
    # create followings fields for CustomUser table(define with type and size)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='freelancer')

    # using this function we can see actual username (if we don't use this function then  in admin panel shows  object not username)
    def __str__(self):
        return self.username


User = get_user_model()  # This ensures compatibility with custom user models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    video = models.URLField(blank=True, null=True, help_text="Link to your intro video (YouTube, etc.)")
    language = models.CharField(max_length=255, blank=True, null=True, help_text="Languages you speak or code in")
    education = models.CharField(max_length=255, blank=True, null=True, help_text="Your educational background")
    job_title = models.CharField(max_length=255, default='Python Developer')
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True, help_text="Portfolio or live project link")
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # <-- New Field


    def __str__(self):
        return self.user.username
 

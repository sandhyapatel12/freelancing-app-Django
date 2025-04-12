from allauth.account.adapter import DefaultAccountAdapter
from django.utils.text import slugify
import random
from .models import UserProfile  # make sure you import this!


# while user login with google at that time not provide username so this adapter generate  unique username using user email and random number
class MyAccountAdapter(DefaultAccountAdapter):
    def generate_unique_username(self, email):
        base_username = slugify(email.split('@')[0])  # Extracts the first part of the email (before @).
        return f"{base_username}{random.randint(1000, 9999)}"  # Add random number to avoid duplicates

    def populate_username(self, request, user):
        if not user.username:  # If username is empty, generate one
            user.username = self.generate_unique_username(user.email)

    # craete userprofile which is login with google
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        
        # Set default user_type if not already set
        if not user.user_type:
            user.user_type = 'freelancer'
        
        if commit:
            user.save()

        # 🔥 Create UserProfile automatically
        UserProfile.objects.get_or_create(user=user)

        return user

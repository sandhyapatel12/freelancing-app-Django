# Generated by Django 5.1.7 on 2025-04-04 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_user_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                ("skills", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_userprofile_job_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

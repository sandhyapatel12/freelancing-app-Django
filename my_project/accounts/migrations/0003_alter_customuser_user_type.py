# Generated by Django 5.1.7 on 2025-04-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20250402_1145"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("client", "Client"), ("freelancer", "Freelancer")],
                default="freelancer",
                max_length=10,
            ),
        ),
    ]

WorkWave – Freelancing Platform (Django Project)

# How to Run the App
---------------------
1. Activate virtual environment:
   > .venv\Scripts\activate
   Example: (freelancing-platform) PS D:\freelancing-platform>

2. Navigate to the project directory:
   > cd .\my_project\
   Example: (freelancing-platform) PS D:\freelancing-platform\my_project>

3. Run the development server:
   > python manage.py runserver


# Creating Django Project and App
----------------------------------
1. Create project:
   > django-admin startproject my_project

2. (Optional) Install uv for fast package management:
   > pip install uv

3. Create virtual environment:
   > uv venv

4. Activate virtual environment:
   > .venv\Scripts\activate

5. Install Django:
   > uv pip install Django

6. Create app inside project:
   > cd my_project
   > python manage.py startapp accounts

Note:
- Project Name: my_project
- App Name: accounts
- Use this path for templates: templates/accounts


# Required Libraries
---------------------
uv pip install Django
python -m pip install Pillow
uv pip install django-allauth
uv pip install sendgrid
uv pip install python-dotenv
uv pip install django-environ


# Installing Tailwind CSS
---------------------------
Option 1 (using uv):
> uv pip install 'django-tailwind[reload]'

Option 2 (using pip if uv fails):
> python -m ensurepip --upgrade
> pip install 'django-tailwind[reload]'

Steps:
1. Add 'tailwind' to INSTALLED_APPS in settings.py
2. Init Tailwind:
   > python manage.py tailwind init
   (Default app name: theme)
3. Add 'theme' to INSTALLED_APPS
4. Add to settings.py:
   TAILWIND_APP_NAME = "theme"
   INTERNAL_IPS = ['127.0.0.1']
   NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
5. Install Tailwind dependencies:
   > python manage.py tailwind install
6. Open second terminal and run:
   > .venv\Scripts\activate
   > cd .\my_project\
   > python manage.py tailwind start
7. Restart both terminals if needed


# Create Admin Superuser
--------------------------
> python manage.py createsuperuser
Username: admin
Password: admin


# Model Changes (Migrations)
------------------------------
1. Make migrations:
   > python manage.py makemigrations accounts
2. Apply migrations:
   > python manage.py migrate


# Steps to Create and Use Models
---------------------------------
1. Create model in models.py
2. Register it in admin.py
3. Add app to INSTALLED_APPS
4. Add views in views.py
5. Add path in urls.py
6. Create superuser
7. Run makemigrations & migrate


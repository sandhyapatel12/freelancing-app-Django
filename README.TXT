# How to run app
---------------

1.  activate virtual env -->  .venv\Scripts\activate
    if activate successfully looks like ((DJANGO_APP) PS D:\DJANGO_PROJECT>)

2. goto project dir(which is our sub project inside main project)  -->   cd .\my_project\ 
    looks like : (DJANGO_APP) PS D:\DJANGO_PROJECT\my_project> 

3.  now run the project --> python manage.py runserver 

------------------------------------------------------------------------------------------------------------------------------


# create Django project and app
----------------------------

1. create project       -->  django-admin startproject my_project(project name)   (create two folder with same name but one inside the another project)

2. after running above first command install uv for fast processing    --> pip install uv 

3. create virtual env   --> uv venv 

4. activate virtual env  --> .venv\Scripts\activate

5. now install django  -->   (freelancing-platform) PS D:\freelancing-platform> uv pip install Djang

6. create app inside main my_project folder          -->  python manage.py startapp accounts(app name)    -->   (freelancing-platform) PS D:\freelancing-platform\my_project> python manage.py startapp my_app

my_project   --> project name   (inside main project, available another project so make sure both project name will be same here: my_project)
my_app       --> app name  (inside my app --> templates --> my_app    make sure our app name and folder name will be same  here : my_app)

# LIB
----------------------------------------

pip install uv                                  --> fast Python package manager
uv venv                                         --> install virtual env
.venv\Scripts\activate                          --> active virtual env
uv pip install Django                           --> install Django
python -m pip install Pillow                    --> support to images  
uv pip install django-allauth                      --> 
uv pip install sendgrid
uv pip install python-dotenv
uv pip install django-environ





------------------------------------------------------------------------------------------------------------------------------------------

#  How to  install tailwind in Django

-- first try with uv (if you install uv)
uv pip install 'django-tailwind[reload]'        --> install tailwind  -- reload for automatic reload (using uv)


-- install pip (if uv not work)
python -m ensurepip --upgrade                   --> install pip if (uv not work)
pip install 'django-tailwind[reload]'           --> install tailwind (using pip)

-- after above steps

1. go to project settings.py file(my_project/settings.py)  in INSTALLED_APPS   add "tailwind"
2. (DJANGO_APP) PS D:\DJANGO_PROJECT\my_project>             --> python manage.py tailwind init               
3. after runnig above command tailwind tell to you app_name --> (stay default name which is "theme" and  press enter)
4. go to project settings.py file(my_project/settings.py)  in INSTALLED_APPS   add "theme"
5. add this lines after INSTALLED_APPS list     --> 
    TAILWIND_APP_NAME = "theme"
    INTERNAL_IPS = ['127.0.0.1']

6. Add this line at the end of settings.py   -->  NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"
7. in terminal -->    python manage.py tailwind install  
8. now tailwind is install in your project but still now work (so, how can start tailwind)
9. open another terminal but make sure our first terminal is already running
10. in this terminal set -->    
    PS D:\DJANGO_PROJECT> .venv\Scripts\activate
    (DJANGO_APP) PS D:\DJANGO_PROJECT> cd .\my_project\
    (DJANGO_APP) PS D:\DJANGO_PROJECT\my_project> 

11. (venv) PS D:\DJANGO\Hello>     -->        python manage.py tailwind start        
12. now restart both terminal(tailwind is working)

-------------------------------------------------
#  set username and password for admin

create superuser  -->  python manage.py createsuperuser
username : admin
password : admin
 

#   when changes in model, before that run following commands
 ---------------------------------------------------------------

first  :    python manage.py makemigrations my_app(app name )    --  This checks your models.py and creates migration files for database changes.
second :    python manage.py migrate                  -- Applies the migration files to your database (creates actual tables).

# basic steps for create model and activate theme
-----------------------------------------------------

1. create model in models.py file
2. register model into admin.py file
3. copy app class name from apps.py and paste into settings.py file in INSTALLED_APPS
4. give valid path on urls.py file
5. define views in views.py file
6. create superuser    --> python manage.py createsuperuser
7. python manage.py makemigrations my_app(app name)
8. python manage.py migrate




app name  : WorkWave

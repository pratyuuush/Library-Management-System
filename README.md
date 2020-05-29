### LIBRARY MANAGEMENT SYSTEM

Developed in Django==1.10

To run this project first clone this repo and if there is Django(1.10) installed then in the cloned directory run 
```
  > python manage.py makemigrations
  > python manage.py migrate
  > python manage.py createsuperuser // to create a superuser to log in to the website as admin 
  > python manage.py runserver
```
And the project will run in https://localhost:8000.

(I would recommend using `virtualenv` or any virtual environment tools to run this project if django1.10 is not installed in your machine so that your machine will not be populated with the stuffs you don't need.)

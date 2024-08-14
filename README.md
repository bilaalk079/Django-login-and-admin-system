A beautiful Django project that i used to practice django.
it has a registration page where you can register new users.
it has a login page where each user can login.
it also has an admin login.

//For the ADMIN.
You register an admin by going to localhost:8000/regadmin.
if you want to login as an admin it is the same login page You will use.
the admin can block and unblock users.
the admin can also delete users.
//The Users
As for the users dashboard I only created a home page where they can view their details .
And a edit profile page where they can edit their profile and save the changes.

// To use this project
Prerequisites
   Python 3.x (install python if you don't have)
   Django (run pip install django in your command prompt)
   XAMPP (for MySQL database install xampp if you don't have).
In VS Code
  run git clone https://github.com/bilaalk079/Django-login-and-admin-system in your terminal.
If you have installed XAMPP
  Start Apache and MySQL from the XAMPP Control Panel.
  Open a web browser and go to http://localhost/phpmyadmin/.
  Create a new database named your-database-name.
in VS CODE
  in the project 
  go to the file named settings.py, navigate to the DATABASE settings and paste
        DATABASES = {
            'default': {
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'your-database-name',
               'USER': 'root',
               'PASSWORD': '',
               'HOST': 'localhost',
               'PORT': '3306',
                }
              }
   only change the database Name.
Go back to Command prompt and run the following
  python manage.py makemigrations 
  python manage.py migrate
  python manage.py runserver
Then go to your web browser and type localhost:8000






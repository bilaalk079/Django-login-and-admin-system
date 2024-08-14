# Django Login and Admin system

To use this project follow the steps below

## Getting Started

### Prerequisites

- Python 3.x
- Django
- XAMPP (for MySQL database)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
 2.**Create and Activate a Virtual Environment:**
   ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3.**Database Setup with XAMPP**

4.**Download and install XAMPP.**

   ##Start XAMPP Services:

   ##Start Apache and MySQL from the XAMPP Control Panel.

   ##Create the Database:

   ##Open a web browser and go to http://localhost/phpmyadmin/.
   
   ##Create a new database named your-database-name.
   
   ##Update Database Settings:

   ###Ensure the following settings in settings.py:
   ```bash
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
```
##Run Migrations:

###Apply the migrations to set up the database schema:
 ```bash
  python manage.py migrate
```
##Run the Development Server:
```bash
python manage.py runserver
```
##Access the Project:

###Open a web browser and go to http://127.0.0.1:8000/ to access the project.
 you can customize 'your-database-name' into any name of your choice

   
 






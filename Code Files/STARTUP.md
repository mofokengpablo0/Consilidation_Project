# News Application Startup Guide

Written by Paballo Mofokeng

## Overview

This is a Django news application built with:
- Django
- Django REST Framework
- Simple JWT authentication
- crispy-forms and Bootstrap 5
- Custom user model in `accounts.CustomUser`

## Project structure

- `news_project/` - Django project root
- `accounts/` - custom user app and account-related logic
- `news/` - news models, views, APIs, templates, and signals
- `news_project/templates/` - base templates and app templates
- `news_project/static/` - application static assets
- `requirements.txt` - Python dependency list

## Local setup

1. Open a terminal in the project root folder.

2. Create and activate a virtual environment if needed:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. If using MariaDB, set the database engine and connection variables before running migrations. Example PowerShell commands for the current session:

```powershell
$env:DB_ENGINE = 'mariadb'
$env:DB_NAME = 'news_db'
$env:DB_USER = 'root'
$env:DB_PASSWORD = 'PABLOSAAS'
$env:DB_HOST = '127.0.0.1'
$env:DB_PORT = '3306'
```

Then apply migrations:

```powershell
python manage.py migrate
```

If you want to keep using SQLite, skip the environment variables and run:

```powershell
python manage.py migrate
```

### Local MariaDB server

If Docker is not available, install MariaDB locally on your computer and start the MariaDB service.

1. Download MariaDB for Windows from https://mariadb.org/download.
2. Install it and set the root password to `PABLOSAAS`.
3. Start the MariaDB service.
4. Verify it is running:

```powershell
mysql -u root -pPABLOSAAS -e "SHOW DATABASES;"
```

Then use the same environment variables above and run migrations.

### Docker Compose (MariaDB)

A `docker-compose.yml` file is included in the project root. Use Docker if you prefer not to install MariaDB locally.

To start MariaDB with Docker:

```powershell
docker compose up -d
```

Then set the same environment variables and run migrations once the container is healthy.

5. Create a superuser (optional but recommended for admin access):

```powershell
python manage.py createsuperuser
```

6. Start the development server:

```powershell
python manage.py runserver
```

7. Open the app in your browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/` for the Django admin site

## Notes

- The app is configured to use SQLite by default.
- For MySQL or MariaDB, set environment variables and use `DB_ENGINE=mysql` in `news_project/news_project/settings.py`.
- Static files are served automatically by Django in development mode.

## Troubleshooting

- If the server reports missing modules, install them with `pip install -r requirements.txt`.
- If migrations are pending, run `python manage.py migrate` again.
- If the app does not load, confirm the virtual environment is active and the correct Python interpreter is used.

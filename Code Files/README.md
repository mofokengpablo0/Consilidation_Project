# News Application

This is a Django news application built with Django, Django REST Framework, Simple JWT, and Bootstrap 5.

## Local setup

1. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Run migrations for SQLite:

```powershell
python manage.py migrate
```

4. Create a superuser:

```powershell
python manage.py createsuperuser
```

5. Start the development server:

```powershell
python manage.py runserver
```

6. Open the app:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`

## MariaDB without Docker

If you do not want to use Docker, install MariaDB locally on your machine.

1. Install MariaDB for Windows from https://mariadb.org/download.
2. Set the root password to `PABLOSAAS` during installation.
3. Start the MariaDB service.
4. Verify the server is running:

```powershell
mysql -u root -pPABLOSAAS -e "SHOW DATABASES;"
```

5. In the same terminal, set the MariaDB environment variables:

```powershell
$env:DB_ENGINE = 'mariadb'
$env:DB_NAME = 'news_db'
$env:DB_USER = 'root'
$env:DB_PASSWORD = 'PABLOSAAS'
$env:DB_HOST = '127.0.0.1'
$env:DB_PORT = '3306'
```

6. Run migrations:

```powershell
python manage.py migrate
```

7. Start the Django app:

```powershell
python manage.py runserver
```

## MariaDB with Docker Compose

A `docker-compose.yml` file is included in the project root. It configures MariaDB with:

- database: `news_db`
- user: `root`
- password: `PABLOSAAS`
- port: `3306`

Start MariaDB with:

```powershell
docker compose up -d
```

Wait for the container to become healthy.

Then set the environment variables for the current PowerShell session:

```powershell
$env:DB_ENGINE = 'mariadb'
$env:DB_NAME = 'news_db'
$env:DB_USER = 'root'
$env:DB_PASSWORD = 'PABLOSAAS'
$env:DB_HOST = '127.0.0.1'
$env:DB_PORT = '3306'
```

Run migrations:

```powershell
python manage.py migrate
```

If the container is running and the credentials are correct, Django will use MariaDB instead of SQLite.

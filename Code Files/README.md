# Consolidation Project — News Application

A Django-based news platform with role-based access (Readers, Journalists, Editors), a REST API, and Sphinx documentation.

## Project Structure

```
Consilidation_Project/
├── Code Files/
│   └── news_project/          # Django project root (contains manage.py)
│       ├── accounts/          # User model, auth, roles
│       ├── news/              # Articles, publishers, newsletters, API
│       ├── news_project/      # Settings package
│       ├── docs/              # Sphinx documentation
│       ├── static/ media/ templates/
│       ├── manage.py
│       ├── requirements.txt
│       ├── Dockerfile
│       ├── docker-compose.yml
│       └── entrypoint.sh
└── README.md                  # This file
```

---

## Option 1: Run with venv (local Python environment)

### Prerequisites
- Python 3.12+
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mofokengpablo0/Consilidation_Project.git
   cd "Consilidation_Project/Code Files/news_project"
   ```

2. **Create and activate a virtual environment**

   Windows (PowerShell):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for `/admin/` access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open the app**
   Visit `http://127.0.0.1:8000` in your browser.

By default this uses SQLite (`db.sqlite3`), no extra database setup required.

---

## Option 2: Run with Docker

Works identically on your local machine, a teammate's machine, or a browser-based environment like [Docker Playground](https://labs.play-with-docker.com/) or [Iximiuz Labs](https://labs.iximiuz.com/) — no local Python or dependency installation needed at all.

### Prerequisites
- Docker and Docker Compose (pre-installed on Docker Playground / Iximiuz Labs; install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for local use)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mofokengpablo0/Consilidation_Project.git
   cd "Consilidation_Project/Code Files/news_project"
   ```

2. **Build and start the container**
   ```bash
   docker compose up --build
   ```

   This will:
   - Build the image from the `Dockerfile`
   - Install all dependencies
   - Collect static files
   - Apply database migrations automatically
   - Start the app via Gunicorn on port `8000`

3. **Open the app**

   - **Local Docker:** visit `http://localhost:8000`
   - **Docker Playground:** click the port badge (or use "OPEN PORT" → `8000`) at the top of the session page
   - **Iximiuz Labs:** click the `+` next to your terminal tabs → **Add HTTP(S) Port Tab** → set Port to `8000`, Protocol to `HTTP` → click **ADD**

4. **Create a superuser** (in a separate terminal, while the app is running)
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

5. **Stop the app**
   ```bash
   docker compose down
   ```
   Add `-v` (`docker compose down -v`) to also remove the database/media volumes and start fully fresh next time.

### Environment variables

Configured in `docker-compose.yml`, can be overridden as needed:

| Variable | Default | Description |
|---|---|---|
| `DB_ENGINE` | `sqlite` | `sqlite`, `mysql`, or `mariadb` |
| `DEBUG` | `True` | Set to `False` for production-style runs |
| `SECRET_KEY` | (insecure default) | Override for any real deployment |
| `ALLOWED_HOSTS` | `*` | Comma-separated list of allowed hostnames |

The app trusts standard reverse-proxy headers (`X-Forwarded-Proto`, `X-Forwarded-Host`), so it works correctly behind any HTTPS-terminating proxy — Docker Playground, Iximiuz, or a production load balancer — without extra configuration.

---

## Documentation

API and code documentation is built with Sphinx. To view it locally:

```bash
cd "Code Files/news_project/docs"
.\make.bat html      # Windows
# or
make html             # macOS/Linux
```

Then open `docs/build/html/index.html` in your browser.

---

## Running Tests

A comprehensive integration test suite is included:

```bash
python test_app.py
```

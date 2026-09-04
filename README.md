# Consolidation Project — News Application

A Django-based news platform with role-based access (Readers, Journalists, Editors), a REST API, and Sphinx documentation.

> **For reviewers:** a working `SECRET_KEY` is provided in [`REVIEWER_SECRETS.txt`](./REVIEWER_SECRETS.txt) at the repo root for grading convenience — copy its contents into a `.env` file (see [Environment variables & secrets](#environment-variables--secrets) below) to run the app immediately without generating your own key. This file will be removed once grading is complete and should not be used for any real deployment.

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

4. **Set up your `SECRET_KEY`** — see [Environment variables & secrets](#environment-variables--secrets) below, then export it in your shell:

   Windows (PowerShell):
   ```powershell
   $env:SECRET_KEY = "<your-generated-key>"
   ```
   macOS/Linux:
   ```bash
   export SECRET_KEY="<your-generated-key>"
   ```

5. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for `/admin/` access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open the app**
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

2. **Create your `.env` file** — see [Environment variables & secrets](#environment-variables--secrets) below.
   ```bash
   cp .env.example .env
   # then edit .env and paste in a real generated SECRET_KEY
   ```
   Reviewers can instead copy the contents of `REVIEWER_SECRETS.txt` straight into `.env` to skip key generation.

3. **Build and start the container**
   ```bash
   docker compose up --build
   ```

   This will:
   - Build the image from the `Dockerfile`
   - Install all dependencies
   - Collect static files
   - Apply database migrations automatically
   - Start the app via Gunicorn on port `8000`

4. **Open the app**

   - **Local Docker:** visit `http://localhost:8000`
   - **Docker Playground:** click the port badge (or use "OPEN PORT" → `8000`) at the top of the session page
   - **Iximiuz Labs:** click the `+` next to your terminal tabs → **Add HTTP(S) Port Tab** → set Port to `8000`, Protocol to `HTTP` → click **ADD**

5. **Create a superuser** (in a separate terminal, while the app is running)
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. **Stop the app**
   ```bash
   docker compose down
   ```
   Add `-v` (`docker compose down -v`) to also remove the database/media volumes and start fully fresh next time.

### Environment variables & secrets

Non-secret settings are configured directly in `docker-compose.yml`:

| Variable | Default | Description |
|---|---|---|
| `DB_ENGINE` | `sqlite` | `sqlite`, `mysql`, or `mariadb` |
| `DEBUG` | `True` | Set to `False` for production-style runs |
| `ALLOWED_HOSTS` | `*` | Comma-separated list of allowed hostnames |

**`SECRET_KEY` is not committed to this repository.** You must supply your own:

1. Copy the example file (if not already done):
   ```bash
   cp .env.example .env
   ```
2. Generate a real Django secret key:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   (If Django isn't installed locally yet, run this inside the venv from Option 1, or via `docker compose run web python -c "..."` using the same command.)
3. Paste the generated value into `.env`:
   ```
   SECRET_KEY=<paste-generated-key-here>
   ```

**Reviewers/graders:** skip steps 1–3 above and instead copy the contents of `REVIEWER_SECRETS.txt` (repo root) directly into `.env` for a working key with zero setup.

`.env` is listed in `.gitignore` and will never be committed.

- **Docker setup:** `.env` is loaded automatically via `env_file` in `docker-compose.yml` — no extra steps needed once the file exists.
- **venv setup:** this project reads settings with plain `os.getenv()`, which does **not** auto-load `.env` files. Export the value directly into your shell instead (see step 4 in [Option 1](#option-1-run-with-venv-local-python-environment) above), or open `.env` and copy the value manually.

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
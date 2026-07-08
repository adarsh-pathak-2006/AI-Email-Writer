# AI Email Writer Backend

This is a Django REST Framework backend for an AI-powered email writing application. It leverages Google's Gemini GenAI to automatically generate context-aware emails based on specified recipient, purpose, tone, and length.

## Features

- **User Authentication**: Secure JWT-based authentication (login/register).
- **AI Email Generation**: Integrates with `google-genai` to generate tailored emails.
- **Email History Dashboard**: Stores and retrieves past generated emails per user.
- **Deployment Ready**: Configured with CORS, environment variables, WhiteNoise/static file support, and database URL configurations.

## Prerequisites

- Python 3.9+
- A Google Gemini API Key.

## Setup Instructions

1. **Clone the repository and navigate to the project directory**
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Copy the `.env.example` file to `.env` and fill in your details:
   ```bash
   cp .env.example .env
   ```
   *Make sure to provide your actual `GEMINI_API_KEY`.*

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- `POST /register/` - Register a new user.
- `POST /token/` - Login and obtain JWT tokens.
- `POST /token/refresh/` - Refresh JWT token.

### Emails (Requires JWT Bearer Token)
- `GET /api/email/` - Retrieve all generated emails for the logged-in user.
- `POST /api/email/` - Generate a new email and save it.
  - **Payload:** `{"recipent": "Name/Role", "purpose": "Meeting", "tone": "Professional", "length": "Short"}`
- `GET /api/email/<id>/` - Retrieve a specific generated email by ID.

## Deployment Notes

This project is configured to be easily deployed on platforms like Render, Heroku, or standard VPS environments:

- **Database**: Uses `dj-database-url` to parse the `DATABASE_URL` environment variable for Postgres connection. It falls back to SQLite if not provided.
- **Static Files**: `STATIC_ROOT` is configured. Run `python manage.py collectstatic` during deployment.
- **CORS**: `django-cors-headers` is installed and configured. In production, consider changing `CORS_ALLOW_ALL_ORIGINS` to `False` and specifically whitelisting your frontend domains in `settings.py`.
- **WSGI/ASGI**: Use `gunicorn ai_email_writer.wsgi` to serve the application in a production environment.

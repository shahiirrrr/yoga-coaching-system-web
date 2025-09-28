# Security Guide

This project is public. Follow these practices to keep your credentials and data safe.

## Secrets Management
- Do NOT commit secrets (passwords, API keys) to source control.
- Store secrets in environment variables using a local `.env` file.
- `.env` is already ignored by `.gitignore`.

### Environment Variables
Create a `.env` in the project root using `.env.example` as a template:
```
# MySQL
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=change_me
MYSQL_DB=yoga

# SMTP (optional; needed only if you enable forgot-password features)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASSWORD=app_specific_password
SMTP_FROM=your_email@example.com
```

## Application Configuration
- `src/dbconnection.py` reads DB credentials from environment variables via `python-dotenv`.
- `src/android.py` uses environment variables for SMTP credentials.
- Recommended: update `src/webcoding.py` forgot-password to also use the same SMTP_* environment variables. See the snippet below.

### Replace hardcoded SMTP in `src/webcoding.py`
Add near the top if not present:
```python
from dotenv import load_dotenv
```
After `app = Flask(__name__)`:
```python
load_dotenv()
```
In `fpp()` replace the SMTP setup with:
```python
smtp_host = os.getenv('SMTP_HOST', 'smtp.gmail.com')
smtp_port = int(os.getenv('SMTP_PORT', '587'))
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')
smtp_from = os.getenv('SMTP_FROM', smtp_user if smtp_user else 'noreply@example.com')

gmail = smtplib.SMTP(smtp_host, smtp_port)
gmail.ehlo()
gmail.starttls()
if smtp_user and smtp_password:
    gmail.login(smtp_user, smtp_password)

# When building the message
msg['From'] = smtp_from
```

## Password Hygiene
- Rotate any secrets that were previously committed. If a password (e.g., MySQL root) ever existed in git history, change it now and update `.env`.
- Prefer per-project DB users with limited privileges over using `root`.

## Git History
- If sensitive data was committed in the past, consider rewriting history:
  - Use BFG Repo-Cleaner or `git filter-repo` to remove leaked secrets.
  - Regardless of history cleanup, rotate the compromised secret.

## Production Considerations
- Do not use Flask debug server in production.
- Use a production WSGI server (e.g., gunicorn/uwsgi) and secure reverse proxy.
- Use strong, unique credentials; never share app passwords.
- Avoid emailing plain-text passwords; use reset tokens and hashed passwords (bcrypt/argon2) for real deployments.

# Yoga Coaching System - Web

A Flask-based web application with MySQL database and an optional webcam-powered yoga pose recognition feature using MediaPipe and OpenCV.

## Prerequisites
- Python 3.10 (recommended)
- MySQL Server running locally
- A webcam (for the pose-recognition feature via `/startcam`)

## Project Structure
- `src/webcoding.py` — Flask app entry point (runs the web server)
- `src/dbconnection.py` — MySQL connection helpers (expects DB `yoga` at `localhost:3306` user `root` password `''`)
- `src/em1.py` — Webcam loop that calls pose recognition
- `src/yoga.py` — Pose detection/classification using MediaPipe & OpenCV
- `src/templates/` — HTML templates
- `src/static/` — Static assets (CSS, JS, images, videos)
- `db.sql` — Database schema/data dump (use this to create `yoga` DB)
- `requirements.txt` — Python dependencies

## Setup (Windows / PowerShell)

1. Create and activate a virtual environment
```
python -m venv .venv
. .venv\Scripts\Activate.ps1
```

2. Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

3. Create the MySQL database
- Start MySQL locally
- Create a database named `yoga`
- Import `db.sql` (or `db final.sql` if that’s the correct dump for your environment)

Example (using MySQL CLI):
```
mysql -u root -p
CREATE DATABASE yoga;
USE yoga;
SOURCE "c:/Projects/Yoga-Coaching-System-Web/db.sql";
```

Note: The app expects MySQL credentials in `src/dbconnection.py`:
```
host='localhost', port=3306, user='root', password='', db='yoga'
```
Adjust this file if your MySQL credentials differ.

4. Run the web app
```
python src/webcoding.py
```
- App starts in debug mode at http://127.0.0.1:5000/
- Login page route: `/`

5. (Optional) Use the webcam pose recognition
- Visit: `http://127.0.0.1:5000/startcam`
- A window will open showing the camera output
- Press `q` to quit the webcam window

## Notes & Tips
- If you see `ModuleNotFoundError`, ensure the virtual environment is active and dependencies are installed.
- For OpenCV + MediaPipe, ensure your webcam drivers are available. If `cv2.VideoCapture(0)` fails, try `1` or `2`.
- Email Forgotten Password (`/fp` -> `/fpp`) uses Gmail SMTP with hardcoded credentials in `src/webcoding.py`. This will likely fail unless you replace with valid environment variables or app passwords. It is not required to run the site locally.
- If templates fail to render, make sure you run from the project root and start via `python src/webcoding.py` so Flask can resolve `src/templates/`.

## Common Errors
- `pymysql.err.OperationalError: (1049, "Unknown database 'yoga'")` — Create the DB and import `db.sql`.
- `Access denied for user 'root'@'localhost'` — Update credentials in `src/dbconnection.py` to match your MySQL setup.
- `cv2` related errors — Ensure OpenCV installed and webcam accessible.

## Further Documentation
- See `docs/HowToRun.md` for step-by-step Windows setup using a Python 3.10 virtual environment and MySQL.
- See `docs/TechStack.md` for a breakdown of the technologies used and version guidance.
- See `docs/ProjectOverview.md` for features, roles, and the project layout.

Note: For reliable MediaPipe support and proper imports, it’s recommended to:
- Use a Python 3.10 virtual environment.
- Start the app from the project root with `python -m src.webcoding`.

## License
This is a student project. No license specified.

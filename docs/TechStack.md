# Tech Stack

This document describes the technologies used in the Yoga Coaching System, with version guidance and role in the project.

## Backend
- Python 3.10 (runtime for this project)
  - Note: Python 3.13 may not have prebuilt wheels for MediaPipe on Windows; use a 3.10 virtual environment.
- Flask 2.3.x
  - Lightweight web framework used in `src/webcoding.py` (web) and `src/android.py` (mobile APIs).
- PyMySQL 1.1.x
  - MySQL database driver used in `src/dbconnection.py` for queries.

## Computer Vision / ML
- OpenCV 4.12.x (opencv-python)
  - Image capture and processing; webcam via `cv2.VideoCapture(0)` in `src/em1.py`.
- MediaPipe 0.10.x
  - Pose estimation to extract landmarks in `src/yoga.py`.
- NumPy 1.24+
  - Array operations used by OpenCV/MediaPipe.
- Matplotlib 3.7+
  - Used for debugging/visualization in `src/yoga.py` (non-essential in production).

## Database
- MySQL Community Server 8.x
  - Schema/data import files: `db.sql`, `db final.sql`.
  - Connection settings in `src/dbconnection.py` (update with your credentials).

## Frontend
- HTML templates in `src/templates/`
  - `admin/` and `trainer/` sections for role-specific pages.
  - Entry pages: `logintmp.html`, `indexlogin.html`, etc.
- Static assets in `src/static/`
  - CSS/JS/images/videos organized under subfolders.

## Project Layout
- `src/webcoding.py`: Web Flask app (admin/trainer web UI)
- `src/android.py`: Mobile API Flask app for user endpoints
- `src/dbconnection.py`: DB helper functions (select/insert/update/delete)
- `src/em1.py`: Webcam loop; calls `maincode` from `src/yoga.py`
- `src/yoga.py`: Pose detection/classification using MediaPipe and OpenCV
- `src/templates/`: HTML templates
- `src/static/`: Static resources
- `db.sql`, `db final.sql`: Database dump files
- `requirements.txt`: Python dependencies

## Why these choices?
- Flask: Simple, fast to prototype, easy to deploy, integrates well with Jinja templates.
- MySQL + PyMySQL: Relational DB, easy local setup for student projects, widely supported.
- MediaPipe + OpenCV: Real-time pose detection with minimal training required; good accuracy for classic poses.

## Known limitations
- Forgot-password flows in `src/webcoding.py` and `src/android.py` use hardcoded Gmail credentials (security risk). Replace with environment variables or a proper mail service.
- User role is primarily served via mobile API (`src/android.py`), not via the web UI.
- MediaPipe and OpenCV need compatible Python/OS builds; Python 3.10 venv recommended.

# Project Overview

The Yoga Coaching System is a Flask-based web application that supports administrative and trainer workflows, with optional user/mobile endpoints and a computer-vision module for yoga pose recognition.

## Goals
- Provide an admin interface to manage trainers, work assignments, users, and complaints.
- Provide a trainer interface to upload videos, manage assigned work, and respond to doubts.
- Offer optional real-time yoga pose recognition via webcam using MediaPipe and OpenCV.
- Expose REST-like endpoints (in a separate Flask app) intended for a mobile client for end users.

## Roles
- Admin (web)
- Trainer (web)
- User (mobile API via `src/android.py`; not a full web UI)

## Key Features
- Admin
  - Manage trainers: add, edit, delete (`/addtrainer`, `/trainermng`, `/edittrainer`, ...)
  - Create and assign work to trainers (`/addwork`, `/assignwork`, `/assigned_work_status`)
  - Manage/monitor users and block/unblock as needed (`/blockunblock`)
  - Handle complaints and send replies (`/complaints`, `/send_reply`)
- Trainer
  - View assigned work and update status (`/TRAINERWORK`, `/updatestatus`)
  - Upload training videos (`/Addvideo`)
  - View and reply to user doubts (`/doubtview`, `/doubtreply`)
- User (mobile API)
  - Register, login, view trainers, send requests, ask doubts, view videos (see `src/android.py` endpoints)
- Pose Recognition
  - Start webcam session to detect/classify basic poses (`/startcam`)

## Architecture
- Web server entry point: `src/webcoding.py`
- Mobile API server: `src/android.py`
- Database access helpers: `src/dbconnection.py`
- Pose recognition: `src/em1.py` and `src/yoga.py`
- Templates: `src/templates/` (Jinja2)
- Static assets: `src/static/`
- Database dumps: `db.sql`, `db final.sql`

## Directory Structure
```
Yoga-Coaching-System-Web/
├─ docs/
│  ├─ HowToRun.md
│  ├─ TechStack.md
│  └─ ProjectOverview.md
├─ src/
│  ├─ __init__.py
│  ├─ webcoding.py         # Web app (admin/trainer)
│  ├─ android.py           # Mobile API endpoints (user role)
│  ├─ dbconnection.py      # MySQL connection helpers
│  ├─ em1.py               # Webcam capture loop
│  ├─ yoga.py              # Pose detection/classification
│  ├─ templates/
│  │  ├─ admin/
│  │  ├─ trainer/
│  │  ├─ logintmp.html
│  │  └─ ...
│  └─ static/
├─ requirements.txt
├─ db.sql
├─ db final.sql
└─ README.md
```

## Data Model (high level)
- `login_table (LOGIN_ID, USER_NAME, PASSWORD, TYPE)`
- `trainer_table (LOGIN_ID, FIRST_NAME, LAST_NAME, GENDER, DOB, PHONE, EMAIL, QUALIFICATION)`
- `user_table (LOGIN_ID, FIRST_NAME, LAST_NAME, GENDER, DOB, PHONE, EMAIL, HEIGHT, WEIGHT, HEALTH)`
- `work_table`, `assignwork_table`
- `video_table`
- `doubt_table`, `compaint_table`
- `request` (user-trainer association requests)

## Notes
- The forgot-password flows use Gmail SMTP with hardcoded credentials; replace with environment variables for security if deploying.
- The user role is available via `src/android.py` endpoints; the web UI focuses on admin and trainer.
- Use `python -m src.webcoding` to run the web UI so that package imports resolve correctly.

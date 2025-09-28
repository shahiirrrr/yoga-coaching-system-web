# How to Run the Yoga Coaching System (Windows)

This guide walks you through running the project locally on Windows with a dedicated Python 3.10 virtual environment and a local MySQL database.

## Prerequisites
- Python 3.10 installed (Python 3.13 may not have MediaPipe wheels)
- MySQL Community Server 8.x
- Git (optional)
- A webcam (optional, for pose recognition via `/startcam`)

## 1) Clone or open the project
```
c:\Projects\Yoga-Coaching-System-Web
```

## 2) Create and activate a Python 3.10 virtual environment
Use the Python launcher to target Python 3.10 specifically.
```powershell
py -3.10 -m venv .venv310
. .venv310\Scripts\Activate.ps1
```
If execution is blocked, run PowerShell as Administrator once:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then re-activate the venv.

## 3) Install dependencies
```powershell
pip install -r requirements.txt
```
The project uses `Flask`, `PyMySQL`, `OpenCV`, `MediaPipe`, `NumPy`, and `Matplotlib`.

## 4) Install and start MySQL
- Install MySQL Community Server (Full or Custom with Server + Workbench)
- Start the MySQL service (usually auto-starts)

## 5) Create the database and import the schema/data
Option A: Workbench (GUI)
- Open MySQL Workbench
- Connect to Local Instance (root)
- Create the schema:
  ```sql
  CREATE DATABASE yoga;
  ```
- Import: Server > Data Import > Import from Self-Contained File
  - File: `c:/Projects/Yoga-Coaching-System-Web/db.sql` (or `db final.sql`)
  - Default Target Schema: `yoga`
  - Start Import

Option B: CLI
```powershell
"C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe" -u root -p
```
Then run:
```sql
CREATE DATABASE yoga;
USE yoga;
SOURCE "c:/Projects/Yoga-Coaching-System-Web/db.sql";
-- or
SOURCE "c:/Projects/Yoga-Coaching-System-Web/db final.sql";
```

## 6) Configure database credentials in the app
Edit `src/dbconnection.py` and ensure all four `pymysql.connect(...)` calls use your real credentials. Example:
```python
pymysql.connect(host='localhost', port=3306, user='root', password='11012003', db='yoga')
```
There are four functions: `iud`, `selectone`, `selectall`, `selectall2`.

## 7) Run the web app
From the project root:
```powershell
python -m src.webcoding
```
- App runs at: http://127.0.0.1:5000/
- Login page route: `/`
- Roles supported in the web UI: `admin`, `trainer` (user APIs are provided in `src/android.py` for mobile usage)

## 8) Optional: webcam pose recognition
Visit:
```
http://127.0.0.1:5000/startcam
```
- A window opens showing the camera output
- Press `q` to quit

## Troubleshooting
- ModuleNotFoundError for `src`: always start the app with `python -m src.webcoding` from the project root.
- MySQL access errors: confirm credentials in `src/dbconnection.py` and that the `yoga` schema exists.
- MediaPipe or OpenCV issues: ensure you used Python 3.10 venv and have a working webcam.
- Forgot password features use Gmail SMTP with hardcoded credentials (not recommended); it may fail locally.

@echo off
REM Quick launcher for subsequent runs (after setup.bat has been run once)
call venv\Scripts\activate.bat
python manage.py runserver

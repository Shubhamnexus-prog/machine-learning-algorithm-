@echo off
echo ============================================
echo   Lingua Backend Setup (Python 3.12)
echo ============================================

REM Check if Python 3.12 is available via the py launcher
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python 3.12 not found via "py -3.12".
    echo Install it from https://www.python.org/downloads/release/python-3120/
    echo Make sure to tick "Add python.exe to PATH" during install.
    pause
    exit /b 1
)

echo.
echo [1/5] Creating virtual environment with Python 3.12...
py -3.12 -m venv venv

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Upgrading pip...
python -m pip install --upgrade pip

echo.
echo [4/5] Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo [5/5] Running database migrations...
python manage.py migrate

echo.
echo ============================================
echo   Setup complete!
echo   Run the server with: venv\Scripts\activate ^&^& python manage.py runserver
echo ============================================
pause

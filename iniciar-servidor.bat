@echo off
echo ================================================
echo  THIAGO BANDEIRA - Preview Local
echo ================================================
echo.
echo Iniciando servidor em http://localhost:5500
echo.
cd /d "%~dp0"
start "" "http://localhost:5500"
python -m http.server 5500
pause

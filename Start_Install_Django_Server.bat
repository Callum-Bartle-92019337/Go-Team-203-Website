@echo off

setlocal
SET /P AREYOUSURE1=Install virtual environments (Y/[N])?
IF /I "%AREYOUSURE1%" NEQ "Y" GOTO VIRTEN

pip install virtualenv 
mkvirtualenv djProject3
:VIRTEN
workon djProject3

SET /P AREYOUSURE1=Install requirements (Y/[N])?
IF /I "%AREYOUSURE1%" NEQ "Y" GOTO REQS

pip install -r requirements.txt

:REQS

echo.
SET /P AREYOUSURE2=Make Migrations to Database (Y/[N])?
IF /I "%AREYOUSURE2%" NEQ "Y" GOTO MIGRA

python manage.py makemigrations
python manage.py migrate

:MIGRA

echo.
SET /P AREYOUSURE3=Make new Super User (Y/[N])?
IF /I "%AREYOUSURE3%" NEQ "Y" GOTO SUPA

python manage.py createsuperuser

:SUPA
echo.
echo.
echo Press any key to exit . . .
pause >nul
endlocal
@echo off
setlocal enabledelayedexpansion
cd /d C:\ProyectoF\glamstore

REM Disable pager
set GIT_PAGER=
set GIT_EDITOR=

REM Add file
git add core/migrations/0042_populate_lotes_and_vencimiento.py
if errorlevel 1 (
    echo Error adding file
    exit /b 1
)

REM Commit
git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"
if errorlevel 1 (
    echo Error committing
    exit /b 1
)

REM Push
git push origin main
if errorlevel 1 (
    echo Error pushing
    exit /b 1
)

echo Success!

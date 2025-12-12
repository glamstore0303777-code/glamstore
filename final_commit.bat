@echo off
setlocal enabledelayedexpansion
set GIT_PAGER=
set PAGER=
set LESS=
cd /d C:\ProyectoF\glamstore
git add core/migrations/0042_populate_lotes_and_vencimiento.py
if !errorlevel! neq 0 (
    echo Error adding file
    exit /b 1
)
git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"
if !errorlevel! neq 0 (
    echo Error committing
    exit /b 1
)
git push origin main
if !errorlevel! neq 0 (
    echo Error pushing
    exit /b 1
)
echo Success!

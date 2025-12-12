@echo off
setlocal
set GIT_PAGER=
set PAGER=
set LESS=
cd /d C:\ProyectoF\glamstore
git add core/migrations/0042_populate_lotes_and_vencimiento.py
git commit -m "Fix migration 0042: Use lowercase column name fechavencimiento for PostgreSQL"
git push origin main
echo Done!
pause

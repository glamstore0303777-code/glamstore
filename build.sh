#!/usr/bin/env bash
# Script de build para Render
set -o errexit

pip install -r requirements.txt

python manage.py migrate

# Cargar datos iniciales si la tabla productos está vacía
python manage.py load_initial_data

python manage.py collectstatic --noinput

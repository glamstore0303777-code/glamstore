#!/bin/bash
set -o errexit

echo "=== Starting GlamStore Build Process ==="

# Run database initialization
echo "1. Initializing database..."
python init_db.py

# Run migrations
echo "2. Running migrations..."
python manage.py migrate

# Collect static files
echo "3. Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Build process completed successfully ==="

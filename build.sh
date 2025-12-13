#!/bin/bash
set -o errexit

echo "=== Starting GlamStore Build Process ==="

# Run migrations
echo "1. Running migrations..."
python manage.py migrate

# Collect static files
echo "2. Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Build process completed successfully ==="

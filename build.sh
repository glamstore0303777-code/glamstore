#!/bin/bash
set -o errexit

echo "=== Starting GlamStore Build Process ==="

# Run database initialization
echo "1. Initializing database..."
python setup_db.py

# Run full data restoration
echo "2. Restoring full data..."
python restore_full_data.py

# Run migrations
echo "3. Running migrations..."
python manage.py migrate

# Collect static files
echo "4. Collecting static files..."
python manage.py collectstatic --noinput

echo "=== Build process completed successfully ==="

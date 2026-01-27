#!/bin/sh

# wait 5 seconds for DB to be ready
sleep 5

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn Project.wsgi

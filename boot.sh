#!/bin/bash
source venv/bin/activate
flask db upgrade
exec gunicorn -w 3 --timeout 300 -b :8000 --access-logfile - --error-logfile - wsgi:app

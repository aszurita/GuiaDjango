web: gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT --log-level info
release: python manage.py migrate && python manage.py collectstatic --noinput
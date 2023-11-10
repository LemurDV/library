set -o nounset

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn core.wsgi -b 0.0.0.0:8310 --timeout=300 --workers=2 --threads=4  --access-logfile -
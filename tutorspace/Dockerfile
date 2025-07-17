FROM python:3.11-slim
WORKDIR /app

# 1) installa dipendenze di sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq-dev gcc postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# 2) installa dipendenze Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) copia il codice
COPY . .

# 4) espone la porta
EXPOSE 8000

CMD ["bash","-lc", "\
  # applica le migrazioni \
  python manage.py migrate --noinput && \
  # crea superuser se non esiste (usa env var) \
  python manage.py shell -c \"\
import os; \
from django.contrib.auth import get_user_model; \
User=get_user_model(); \
uname=os.environ.get('DJANGO_SUPERUSER_USERNAME'); \
email=os.environ.get('DJANGO_SUPERUSER_EMAIL'); \
pwd=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); \
uname and not User.objects.filter(is_superuser=True).exists() and \
User.objects.create_superuser(uname,email,pwd)\" && \
  # raccogli static files \
  python manage.py collectstatic --noinput && \
  # infine avvia Gunicorn \
  exec gunicorn tutorspace.wsgi:application --bind 0.0.0.0:8000 \
"]



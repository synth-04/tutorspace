# Dockerfile

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      libpq-dev \
      gcc \
 && rm -rf /var/lib/apt/lists/*

# Installa dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il progetto
COPY . .

# Espone la porta 8000
EXPOSE 8000

# Comando di default: avvia il server Django
CMD ["sh", "-c", "\
  # Migrazioni \
  python manage.py migrate --noinput && \
  # Creazione superuser se non esiste \
  python manage.py shell -c \"\
from django.contrib.auth import get_user_model; \
import os; \
User=get_user_model(); \
if os.getenv('DJANGO_SUPERUSER_USERNAME') and not User.objects.filter(is_superuser=True).exists(): \
    User.objects.create_superuser(os.getenv('DJANGO_SUPERUSER_USERNAME'),os.getenv('DJANGO_SUPERUSER_EMAIL'),os.getenv('DJANGO_SUPERUSER_PASSWORD'))\" && \
  # Raccolta statici \
  python manage.py collectstatic --noinput && \
  # Avvio Gunicorn \
  gunicorn tutorspace.wsgi:application --bind 0.0.0.0:8000 \
"]


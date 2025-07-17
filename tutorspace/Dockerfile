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
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn tutorspace.wsgi:application --bind 0.0.0.0:8000"]


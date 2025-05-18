# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Installa dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il progetto
COPY . .

# Espone la porta 8000
EXPOSE 8000

# Comando di default: avvia il server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

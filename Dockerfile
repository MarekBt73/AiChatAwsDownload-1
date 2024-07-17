FROM python:3.10-slim

# Zainstalowanie wymaganych pakietów systemowych
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    pkg-config

# Zainstalowanie postgresql-client
RUN apt-get update && apt-get install -y postgresql-client

# Ustawienie zmiennej środowiskowej PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Aktualizacja pip
RUN pip install --upgrade pip

# Skopiowanie pliku requirements.txt do katalogu roboczego
COPY requirements.txt /app/

# Instalacja zależności
RUN pip install -r requirements.txt

# Skopiowanie całej aplikacji do katalogu roboczego
COPY . /app/

# Uruchomienie aplikacji z oczekiwaniem na gotowość bazy danych
CMD ["sh", "-c", "until pg_isready -h db_chat_container -p 5432 -U marekbecht; do echo 'Waiting for db to be ready...'; sleep 2; done && python manage.py runserver 0.0.0.0:9000"]

#!/bin/sh

set -e

echo "helooo $POSTGRES_HOST $POSTGRES_PORT"

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for PostgreSQL start..."
    sleep 2
done

echo "PostgreSQL server started"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000

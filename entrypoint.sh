#!/bin/sh

while ! nc -z $MYSQL_HOST $MYSQL_PORT ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
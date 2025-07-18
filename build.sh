#!/usr/bin/env bash

# Virtual environment yaratish
python -m venv venv
source venv/bin/activate

# Kutubxonalarni o‘rnatish
pip install -r requirements.txt

# Django komandalar
python manage.py migrate
python manage.py collectstatic --noinput

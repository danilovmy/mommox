FROM python:latest

## Create a group and user

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

## Install and test.
ARG DJANGO_SUPERUSER_PASSWORD=test
ARG DJANGO_SUPERUSER_EMAIL=test@test.com

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

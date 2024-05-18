FROM python:3.9-alpine

ENV PYTHONestic 1

COPY requirements.txt .

RUN mkdir /app

WORKDIR /app

COPY . .

CMD python manage.py runserver 0.0.0.0:8000 
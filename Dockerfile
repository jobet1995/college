FROM python:3.9-alpine

ENV PYTHONestic 1

COPY requirements.txt .

RUN mkdir /app

WORKDIR /app

COPY . .

RUN python manage.py collectstatic --noinput

ENV UWSGI_WSGI_FILE=./config/wsgi.py

ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

ENV UWSGI_STATIC_MAP="/static/=/code/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

RUN python manage.py migrate --noinput

CMD python manage.py runserver 0.0.0.0:8000 
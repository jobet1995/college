FROM python:3.9-alpine

ENV PYTHONestic 1

COPY requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
    && runDeps="$( \
    scanelf --needed --nobanner --recursive /usr/local \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

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
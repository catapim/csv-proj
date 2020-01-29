FROM python:3.7-alpine
COPY requirements.txt requirements.txt
RUN whoami
RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base
RUN pip install psycopg2-binary

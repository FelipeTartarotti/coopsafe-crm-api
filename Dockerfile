FROM python:3.8-alpine

MAINTAINER Mutualtech

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev 
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /crm-api
WORKDIR /crm-api
COPY crm-api /crm-api

RUN adduser -D user
USER user


FROM python:3.9-alpine3.13
LABEL maintainer="jjbeekman"

ENV PYTHONUNBUFFERED 1
ARG DEV=false

EXPOSE 8000
ENV PATH="/py/bin:$PATH"

COPY ./tox.ini tox.ini
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; then pip install -r /tmp/requirements.dev.txt; fi &&\
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

COPY app /app
WORKDIR /app

USER django-user
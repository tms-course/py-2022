FROM python:3.8.0-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# ENV WORKON_HOME $HOME/.venv

WORKDIR /app/src

RUN apt-get update -qq && apt-get install \
    build-essential postgresql-client libpq-dev python python3-dev -y

COPY ./tgbot/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./tgbot .

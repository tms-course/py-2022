FROM python:3.8.0-slim as base

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV WORKON_HOME $HOME/.venv
ENV PATH $HOME/.local/bin:$PATH

WORKDIR /app/src
COPY ./tgadmin .

RUN apt-get update -qq && apt-get install build-essential g++ libssl-dev \
  postgresql-client libpq-dev python python3-dev -y

COPY ./tgadmin/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
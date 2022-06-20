FROM python:3.10-slim

RUN apt update && apt install -y --no-install-recommends \
  curl \
  git \
  netcat

RUN pip install --upgrade pip

WORKDIR /app

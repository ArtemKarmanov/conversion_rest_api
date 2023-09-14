FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /converter

RUN pip install --upgrade pip

COPY requirements.txt .env ./
RUN pip install -r requirements.txt

COPY converter .

FROM python:2.7-alpine
WORKDIR /app

# ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .




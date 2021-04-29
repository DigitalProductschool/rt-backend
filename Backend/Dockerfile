# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT app:app --workers 3 --threads 8 --timeout 60
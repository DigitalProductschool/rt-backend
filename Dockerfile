# Dockerfile
FROM python:3.7-stretch
RUN apt-get update -y
# For wkhtmltopdf
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar vxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN cp wkhtmltox/bin/wk* /usr/local/bin/
# libssl1.0-dev is used for wkhtmltopdf
RUN apt-get install -y python-pip python-dev build-essential libssl1.0-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT run:app --workers 1 --threads 8 --timeout 0
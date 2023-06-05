FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/code
RUN mkdir /opt/requirements
WORKDIR /opt/code

ADD requirements /opt/requirements
RUN apt update && apt install build-essential python3-dev libpq-dev libffi-dev cron libjpeg-dev zlib1g-dev python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0 libgtk-3-dev gcc -y
RUN pip install -r /opt/requirements/development.txt
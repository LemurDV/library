FROM python:3.10-slim

ARG GIT_SSL_NO_VERIFY=true
ARG GIT_SSL_NO_VERIFY=true

ENV PYTHONUNBUFFERED 1
WORKDIR /apps

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends telnet curl dos2unix && \
    apt-get clean \

RUN apt-get install -y --no-install-recommends git build-essential

RUN apt-get install gunicorn -y

COPY requirements requirements

COPY . .

RUN pip install --upgrade setuptools

RUN pip install --no-cache-dir -r requirements/base.txt

CMD bash gunicorn.sh


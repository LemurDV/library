FROM python:3.10-slim

ARG GIT_SSL_NO_VERIFY=true
ARG GIT_SSL_NO_VERIFY=true

WORKDIR /apps


COPY requirements requirements

COPY . .

RUN pip install --upgrade setuptools

RUN pip install --no-cache-dir -r requirements/base.txt

CMD bash gunicorn.sh


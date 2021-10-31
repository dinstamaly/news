FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apt-get update \
    && apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev

RUN mkdir /code
WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

